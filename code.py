import os
import shutil
import sys

def copy_one_gz_file(src_folder, dest_folder):
    gz_files = [f for f in os.listdir(src_folder) if f.endswith('.gz')]
    if gz_files:
        src_file = os.path.join(src_folder, gz_files[0])
        dest_file = os.path.join(dest_folder, gz_files[0])
        shutil.copy2(src_file, dest_file)
        print(f"Copied: {src_file} → {dest_file}")

def main(source_root):
    if not os.path.isdir(source_root):
        print("❌ Provided path is not a valid directory.")
        return

    base_output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(base_output_dir, exist_ok=True)

    for root, dirs, files in os.walk(source_root):
        # Create corresponding path in output folder
        rel_path = os.path.relpath(root, source_root)
        target_dir = os.path.join(base_output_dir, rel_path)
        os.makedirs(target_dir, exist_ok=True)

        has_gz = any(f.endswith('.gz') for f in files)
        has_dirs = len(dirs) > 0

        # If .gz files are present, copy one
        if has_gz:
            copy_one_gz_file(root, target_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python copy_gz_structure.py /path/to/source/folder")
    else:
        main(sys.argv[1])
