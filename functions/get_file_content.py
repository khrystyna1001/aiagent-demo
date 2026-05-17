import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        print(f"Error: {file_path} is not in the working directory {working_directory}.")
    
    if not os.path.isfile(abs_file_path):
        print(f"Error: {file_path} is not a file.")

    file_content_string = ""    
    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" content truncated at {MAX_CHARS} characters]'
                )
    
        return file_content_string
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory, with a maximum character limit to prevent excessive output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file whose content is to be retrieved, relative to the working directory",
            ),
        },
    ),
)