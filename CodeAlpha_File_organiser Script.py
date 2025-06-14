import os
import shutil

# Insert your own file path here
folder_path = r" "

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # code skips if folder is detected
    if os.path.isdir(file_path):
        continue
    if filename.endswith(".jpg") or filename.endswith(".png"):
        desk_folder = os.path.join(folder_path, "Images")
    elif filename.endswith(".pdf") or filename.endswith(".docx" or ".docs" or ".txt"):
        desk_folder = os.path.join(folder_path, "Documents")
    else:
        continue

    if not os.path.exists(desk_folder):

        # Create the folder if it doesn't exist
        os.makedirs(desk_folder, exist_ok=True)

    source_file = os.path.join(folder_path, filename)

    # code builds a destination path
    destination_file = os.path.join(folder_path, filename)

    # code moves file
    shutil.move(source_file, destination_file)
print("Process is running")
print("Files organised Successfully")
