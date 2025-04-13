import os

def rename_files_naturally(folder_path, extension=".pgn", padding=3):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(extension)]
    files.sort()  # Or use natsorted(files) if needed for mixed names

    for idx, filename in enumerate(files, start=1):
        new_name = f"{str(idx).zfill(padding)}{extension}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

# Example usage
rename_files_naturally("C:/Users/Student/Desktop/Python programs/Chess book/pgn_folder")
