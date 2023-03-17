import os
import shutil
import glob
import sys

# Initializing variables
if (len(sys.argv) >= 3):
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    verbose = len(sys.argv) == 4 and sys.argv[3] == '--verbose'
else:
    input_path = "./files"
    output_path = "./output"
    verbose = False

if verbose:
    print('[+] start copying files from input folder: ' + input_path + ' to ouput folder: ' + output_path)

"""
Creates a folder if it's not exist
"""
def mkdir(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
"""
Returns language name from given filename
"""
def getLangName(filename)-> str:
    return filename.split('-')[0] 

# Creates output folder
mkdir(output_path)
    
files = os.listdir(input_path)

result = set(map(getLangName, files))

for lang in result:
    output_folder = output_path + '/' + lang
    mkdir(output_folder)
    for file in glob.glob(input_path + '/' + lang + '-*.txt'):
        shutil.copy(file, output_folder)
    if verbose:
        print('[+] Language files ' + lang + ' copied successfully to ' + output_folder)
if verbose:
    print('[+] Finished copying files from ' + input_path + ' to ' + output_path)