import os
import shutil

principal = r"C:\Python\File Management\Principal"
objetivo = r"C:\Python\File Management\Nova pasta"

for root, subdirs, files in os.walk(principal):
    print("root", root)
    print("subdirs", subdirs)
    print("files", files)
    for file in files:
        path = os.path.join(root, file)
        shutil.move(path, objetivo)
