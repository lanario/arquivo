import os

# Defina as extensões de arquivo que deseja organizar
image_types = ['.jpg', '.jpeg', '.png']
zip_types = ['.zip', '.tar', '.7z']
exe_types = ['.exe']

base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'Downloads')

# Verifique e crie o diretório 'jpg' se ele não existir
image_dir = os.path.join(path, 'jpg')
if not os.path.exists(image_dir):
    os.mkdir(image_dir)

# Verifique e crie o diretório 'zip' se ele não existir
zip_dir = os.path.join(path, 'zip')
if not os.path.exists(zip_dir):
    os.mkdir(zip_dir)
    
# Verifique e crie o diretório 'exe' se ele não existir
exe_dir = os.path.join(path, 'exe')
if not os.path.exists(exe_dir):
    os.mkdir(exe_dir)
    

# Obtenha uma lista de todos os arquivos no diretório Downloads
full_list = os.listdir(path)

# Organize os arquivos com base em suas extensões de arquivo
for file in full_list:
    file_extension = os.path.splitext(file)[-1]
    if file_extension in image_types:
        # Move arquivos de imagem para o diretório 'jpg'
        old_path = os.path.join(path, file)
        new_path = os.path.join(image_dir, file)
        os.replace(old_path, new_path)
    elif file_extension in zip_types:
        # Move arquivos ZIP para o diretório 'zip'
        old_path = os.path.join(path, file)
        new_path = os.path.join(zip_dir, file)
        os.replace(old_path, new_path)
    elif file_extension in exe_types:
        # Move arquivos exe para o diretório 'exe', mas apenas se não forem arquivos ZIP
        if not os.path.exists(os.path.join(zip_dir, file)):
            old_path = os.path.join(path, file)
            new_path = os.path.join(exe_dir, file)
            os.replace(old_path, new_path)
