import os
import shutil
source = "message.txt"
dest = "text.txt"
os.rename(source,dest)
print("source path renamed to destination path succesfully")