#coding=utf8

import os
import random
path = os.getcwd()

def removedirsEx(path):
    if os.path.isdir(path):
        filelist = os.listdir(path)
        for file in filelist:
            if os.path.isdir(os.path.join(path, file)):
                removedirsEx(os.path.join(path, file))
            else:
                os.remove(os.path.join(path, file))
        os.removedirs(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        return False

    return True

flist = os.listdir(path)
dirlist = ['dictionaries'] #排除文件夹
for f in flist:
    if os.path.isfile(os.path.join(path, f)):
        file = ''
        flag = False
        for x in f[::-1]:
            if x != '.':
                if flag: file = x + file
            else:
                flag = True
        if len(file) > 0: dirlist.append(file + '.sdr')

for d in flist:
    if os.path.isdir(os.path.join(path, d)):
        if not (d in dirlist):
            print(removedirsEx(os.path.join(path, d)), d)

print('Done!')
