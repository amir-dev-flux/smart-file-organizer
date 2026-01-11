# Smart File Organizer

A Python utility that automatically organizes files in a folder into structured categories such as Images, Documents, Audio, Videos, Installers, and more.

## Features

- Organizes files by type (Images, Documents, Word, Presentations, etc.)
- Automatically creates folders if they don’t exist
- Moves existing folders into a separate `Folders/` directory
- Safe to run multiple times (does not break existing structure)
- Handles unknown file types using an `Others/` folder

## Categories Supported

- Images: jpg, png, jpeg, gif, webp
- Documents: pdf, txt
- Word: doc, docx
- Presentations: ppt, pptx
- Videos: mp4, mkv, avi
- Audio: mp3, wav
- Web: html, css, js
- Archives: zip, rar, 7z
- Installers: exe, msi

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/amir-dev-flux/smart-file-organizer.git
cd smart-file-organizer
```

2. Run the script:

```bash
python src/organizer.py
```

3. Enter the folder path when prompted.

Why I built this

This project was built as part of a project-based learning approach to strengthen my Python fundamentals, file handling, and real-world problem solving.
