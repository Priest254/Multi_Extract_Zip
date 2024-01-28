import zipfile as zf
import os
'''
Automatically extract multiple zip files within a given folder

'''
def extract__(input_dir,output_dir):
    list_files = os.listdir(input_dir)
    for zip_f in list_files:
        print(f"opening {zip_f}")
        with zf.ZipFile(f'{input_dir}\{zip_f}', 'r') as zip_ref:
            zip_ref.extractall(output_dir)

extract__(input("input Directory: "),input("Output Directory: "))
