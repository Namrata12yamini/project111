import shutil
import os
from_dir = "C:/Users/shyam/Downloads/"
to_dir = "C:/Document_Files/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    
