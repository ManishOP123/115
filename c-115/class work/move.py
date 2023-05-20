import os
import shutil
source = "message.txt"
dest = "messages.txt"
shutil.move(source,dest)
print("source path moved to destination path succesfully")