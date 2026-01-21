#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_RULES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "archives": {".zip", ".tar", ".gz", ".tgz", ".7z", ".rar"},
    "executables": {".exe", ".msi"},
}


def unique_destination(dest: Path) -> Path:
    """Se o arquivo já existir no destino, cria um novo nome: 'name (1).ext'."""
    if not dest.exists():
        return dest

    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent

    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def get_destination_folder(ext: str, rules: dict[str, set[str]]) -> str | None:
    ext = ext.lower()
    for folder, exts in rules.items():
        if ext in exts:
            return folder
    return None


def iter_files(base: Path, recursive: bool):
    if recursive:
        yield from (p for p in base.rglob("") if p.is_file())
    else:
        yield from (p for p in base.iterdir() if p.is_file())


def organize_downloads(
    base_dir: Path,
    rules: dict[str, set[str]] = DEFAULT_RULES,
    dry_run: bool = False,
    recursive: bool = False,
) -> dict[str, int]:
    if not base_dir.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {base_dir}")
    if not base_dir.is_dir():
        raise NotADirectoryError(f"Não é um diretório: {base_dir}")

    moved_counts: dict[str, int] = {folder: 0 for folder in rules}
    moved_counts["skipped"] = 0

    for file_path in iter_files(base_dir, recursive=recursive):
        ext = file_path.suffix.lower()
        folder = get_destination_folder(ext, rules)

        if not folder:
            moved_counts["skipped"] += 1
            continue

        dest_dir = base_dir / folder
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest_path = unique_destination(dest_dir / file_path.name)

        if dry_run:
            print(f"[DRY-RUN] {file_path} -> {dest_path}")
        else:
            shutil.move(str(file_path), str(dest_path))
            print(f"[MOVED]   {file_path.name} -> {folder}/")

        moved_counts[folder] += 1

    return moved_counts


def main():
    parser = argparse.ArgumentParser(
        description="Organiza arquivos em uma pasta (ex: Downloads) por extensão."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.home() / "Downloads",
        help="Pasta base para organizar (padrão: ~/Downloads)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula o que seria feito sem mover arquivos",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Também organiza arquivos dentro de subpastas",
    )

    args = parser.parse_args()

    counts = organize_downloads(
        base_dir=args.path,
        dry_run=args.dry_run,
        recursive=args.recursive,
    )

    print("\nResumo:")
    for k, v in counts.items():
        print(f" - {k}: {v}")


if __name__ == "__main__":
    main()
