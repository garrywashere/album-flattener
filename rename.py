import os
import shutil
import xxhash

source_dir = "./photos"
dest_dir = "./renamed"

os.makedirs(dest_dir, exist_ok=True)

file_count = 0

for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)

        folder_name = os.path.basename(root)

        with open(file_path, "rb") as f:
            file_hash = xxhash.xxh64(f.read()).hexdigest()[:6]

        new_file_name = f"{folder_name} - {file_hash}{os.path.splitext(file)[1]}"
        dest_path = os.path.join(dest_dir, new_file_name)

        shutil.copy2(file_path, dest_path)
        file_count += 1

print(f"{file_count} files copied and renamed succesfully.")
