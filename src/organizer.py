import os
import shutil

print("Smart File Organizer starting...")

folder_path = input("Enter folder path to organize: ").strip()

if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

print("\nOrganizing files...\n")

# Categories with extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".txt"],
    "Word": [".doc", ".docx"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Web": [".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi"]
}

# All folders created by the script (to protect them)
SYSTEM_FOLDERS = set(CATEGORIES.keys()) | {"Others", "Folders"}

def ensure_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

files = os.listdir(folder_path)

for item in files:
    item_path = os.path.join(folder_path, item)

    # Handle folders safely
    if os.path.isdir(item_path):
        # Skip system folders created by this script
        if item in SYSTEM_FOLDERS:
            continue

        folders_dir = os.path.join(folder_path, "Folders")
        ensure_folder(folders_dir)
        shutil.move(item_path, os.path.join(folders_dir, item))
        print(f"Moved folder: {item} → Folders/")
        continue

    filename, extension = os.path.splitext(item)
    extension = extension.lower()

    moved = False

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            category_folder = os.path.join(folder_path, category)
            ensure_folder(category_folder)
            shutil.move(item_path, os.path.join(category_folder, item))
            print(f"Moved: {item} → {category}/")
            moved = True
            break

    if not moved:
        others_folder = os.path.join(folder_path, "Others")
        ensure_folder(others_folder)
        shutil.move(item_path, os.path.join(others_folder, item))
        print(f"Moved: {item} → Others/")
