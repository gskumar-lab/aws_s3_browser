import os

def print_directory_tree(start_path='.', prefix=''):
    entries = sorted(os.listdir(start_path))
    entries = [e for e in entries if not e.startswith('.')]  # skip hidden files/folders

    for index, entry in enumerate(entries):
        full_path = os.path.join(start_path, entry)
        is_last = index == len(entries) - 1
        connector = '└── ' if is_last else '├── '

        print(prefix + connector + entry)

        if os.path.isdir(full_path):
            extension = '    ' if is_last else '│   '
            print_directory_tree(full_path, prefix + extension)

if __name__ == '__main__':
    print("Directory structure:")
    print_directory_tree()
