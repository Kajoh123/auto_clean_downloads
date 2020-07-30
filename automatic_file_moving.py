import os
import shutil
import time

pathe = os.path.join('D:\\', 'Downloads')
print(os.listdir(pathe))
while(1):
    try:
        for filename in os.listdir(pathe):
            if(filename.find('.') != -1):
                end = len(filename)
                extension = filename[filename.find('.') + 1: end]
                if extension.find('crdownload') == -1:
                    if not extension in os.listdir(pathe):
                        print(extension)
                        os.mkdir(os.path.join(pathe, extension))
                    shutil.move(os.path.join(pathe, filename), os.path.join(pathe, extension, filename))
    except(PermissionError):
        print('PermissionError!')
    time.sleep(15)