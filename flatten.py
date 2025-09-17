from rich.progress import Progress
import os, shutil, xxhash
from rich import print

source_dir = "./input"
dest_dir = "./output"


def count_files(base_dir):
    return sum(len(files) for _, _, files in os.walk(base_dir))


def flatten(p, task_id):
    os.makedirs(dest_dir, exist_ok=True)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            folder_name = os.path.basename(root)
            with open(file_path, "rb") as f:
                file_hash = xxhash.xxh64(f.read()).hexdigest()[:6]
            new_file_name = f"{folder_name} - {file_hash}{os.path.splitext(file)[1]}"
            dest_path = os.path.join(dest_dir, new_file_name)
            shutil.copy2(file_path, dest_path)
            p.update(task_id, advance=1)


if __name__ == "__main__":
    print("\n" + "=" * 10, "[yellow]Album Flattener[/yellow]", "=" * 11 + "\n")
    print(" " * 10, "© 2025 garrynet", " " * 11 + "\n")
    try:
        total_files = count_files(source_dir)
        if total_files == 0:
            raise FileNotFoundError("Source Directory Empty.")
        with Progress() as p:
            t = p.add_task("[*] Processing...", total=total_files)
            flatten(p, t)
        print(
            f"\n[[green]+[/green]] {total_files} files renamed and copied. :thumbs_up:\n"
        )
    except Exception as e:
        print(
            "[[red]-[/red]] [red]ERROR[/red]: The script has encountered an error. Details [bold]should[/bold] be listed below.\n"
        )
        print(str(e) + "\n")

    print("=" * 10, "[yellow]Program Finished[/yellow]", "=" * 10 + "\n")
