import os
import shutil

# Mapping of file extensions to folder names
EXTENSION_MAP = {
    '.txt': 'TextFiles',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.xlsx': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.mp3': 'Audio',
    '.mp4': 'Videos',
    '.zip': 'Archives'
}

def organize_folder(path):
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory.")
        return

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            folder = EXTENSION_MAP.get(ext.lower())
            if folder:
                dest_folder = os.path.join(path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(file_path, dest_path)
                print(f"Moved '{file}' to '{folder}/'")
            else:
                print(f"Skipping '{file}' (no matching folder)")

if __name__ == "__main__":
    target_path = input("Enter the directory to organize: ").strip()
    organize_folder(target_path)
    print("Organization complete.")
