import os
import shutil

# Ask user to give any folder path
folder_path = input("Enter the full folder path to organize: ")

# Define file categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.mkv', '.avi'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
}

if os.path.exists(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        found = False

        for category, extensions in file_types.items():
            if ext in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)  # Create folder if not exists

                shutil.move(file_path, os.path.join(category_folder, filename))  # Move file
                print(f"Moved: {filename} → {category}/")
                found = True
                break

        if not found:
            others_folder = os.path.join(folder_path, 'Others')
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} → Others/")
else:
    print("❌ This folder path doesn't exist.")
