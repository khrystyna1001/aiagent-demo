import os
import subprocess
from google.genai import types

def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_directory.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the working directory {working_directory}."
    if not os.path.isfile(abs_directory):
        return f"Error: {file_path} is not a file."
    if not file_path.endswith(".py"):
        return f"Error: {file_path} is not a Python file."
    
    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            )
        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """

        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}."

        return final_string
    
    except Exception as e:
        return f"Error running {file_path}: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python file relative to the working directory with optional command-line arguments, capturing and returning the standard output and error, while enforcing security constraints to prevent access outside the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file whose content is to be retrieved, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings that represent command-line arguments to be passed to the Python file when executed",
                items=types.Schema(
                    type=types.Type.STRING
                ),
            ),
        },
    ),
)