import os
import shutil
 
current_dir = os.getcwd()
 
for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)
 
    try:
        if not file_ext:
            pass
 
        elif file_ext in ('.jpg', '.png', '.gif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Photos', f'{filename}{file_ext}'))

        elif file_ext in ('.exe', '.msi'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Softwares', f'{filename}{file_ext}'))

        elif file_ext in ('.zip', '.rar', '.7zip'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Compressed', f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Others', f'{filename}{file_ext}'))                        
 
    except (FileNotFoundError, PermissionError)        :
        pass