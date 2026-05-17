import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_directory.startswith(abs_working_dir):
        print(f"Error: {file_path} is not in the working directory {working_directory}.")
    
    if not os.path.isfile(os.path.dirname(abs_directory)):
        parent_dir = os.path.dirname(abs_directory)
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            print(f"Error creating parent directory {parent_dir}: {e}")
        print(f"Error: The directory for {file_path} is not a file.")
    
    try:
        with open(abs_directory, 'w') as f:
            f.write(content)
        return f"Successfully wrote to '{file_path}' ({len(content)}) characters."
    except Exception as e:
        return f"Error writing to file {file_path}: {e}"