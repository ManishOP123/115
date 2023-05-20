import os
import shutil
source = "message.txt"
dest = "newfile.txt"
os.rename(source,dest)
print("source path renamed to destination path succesfully")