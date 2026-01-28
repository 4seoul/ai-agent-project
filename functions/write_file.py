import os

from google.genai import types

def write_file(working_directory, file_path, content):
	try:
		abs_working_dir = os.path.abspath(working_directory)
		abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
		if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
		if os.path.isdir(abs_file_path):
			return f'Error: Cannot write to "{file_path}" as it is a directory'
	
		os.makedirs(file_path, exist_ok=True)
	
		with open(abs_file_path, "w") as f:
			f.write(content)
			return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
			
	except Exception as e:
		return f"Error: {e}"
		
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes input content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write files from",
                ),
            "content" : types.Schema(
            	type=types.Type.STRING,
            	description="Content that is to be written to the file",
            ),
        },
    ),
)