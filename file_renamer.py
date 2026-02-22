import os

def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)
    
    for index, file in enumerate(files):
        file_extension = os.path.splitext(file)[1]
        new_name = f"{prefix}_{index+1}{file_extension}"
        
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        
        os.rename(old_file, new_file)

    print("Files renamed successfully!")

# Example usage:
folder = "your_folder_path_here"
prefix_name = "renamed_file"

rename_files(folder, prefix_name)
