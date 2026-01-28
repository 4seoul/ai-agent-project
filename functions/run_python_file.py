import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
	try:
		abs_working_dir = os.path.abspath(working_directory)
		abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
		if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
		if not os.path.isfile(abs_file_path):
			return f'Error: "{file_path}" does not exist or is not a regular file'
		if not file_path.endswith('.py'):
			return f'Error: "{file_path}" is not a Python file'
	
		command = ["python", abs_file_path]
	
		cp = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=abs_working_dir)
		
		output = []
		
		if cp.returncode != 0:
			output.append(f"Process exited with code {cp.returncode}")
	
		if not cp.stdout and not cp.stderr:
			output.append(f"No output produced")
	
		if cp.stdout:
			output.append(f"STDOUT:\n{cp.stdout}")
			
		if cp.stderr:
			output.append(f"STDERR:\n{cp.stderr}")
	
		return "\n".join(output)
		
	except Exception as e:
		return f"Error: executing Python file: {e}"
		
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs and returns the output of a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to execute files from",
                ),
            "args": types.Schema(
            	type=types.Type.ARRAY,
            	description="Array of args",
            	items=types.Schema(
            		type=types.Type.STRING,
            		description="items in array"
            		
            	),
            ),
        },
    ),
)
		
	