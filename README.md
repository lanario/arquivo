# Organizador de Downloads (Python)

Script em Python para organizar arquivos em uma pasta (ex: `~/Downloads`) movendo-os para subpastas com base na extensão.

## Funcionalidades
- Organiza por categorias (ex: `images`, `archives`, `executables`)
- Extensões **case-insensitive** (`.PNG`, `.JPG`, etc.)
- Ignora pastas (processa apenas arquivos)
- Cria as pastas automaticamente
- Evita sobrescrever arquivos (gera `arquivo (1).ext`, `arquivo (2).ext`...)
- Modo seguro `--dry-run` (simula sem mover)
- Opção `--recursive` para organizar também subpastas

## Requisitos
- Python 3.10+ (recomendado)
- Sem dependências externas (somente biblioteca padrão)

## Como usar

### 1) Rodar no padrão (~/Downloads)
```bash
python organizer.py
