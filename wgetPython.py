import os, os.path, urllib.request, time

File,savePath,fileName = '','INSERT_PATH_TO_FILE_WITH_URL','FILENAME_TO_READ' #FILENAME = README_urlAdress.txt
completeName = os.path.join(savePath,fileName)
File = open(completeName,'r')

while True:
    line0 = File.readline()
    time.sleep(1)
    if len(line0)>100:
        newUrl = line0.split('\t')
        flagUrlOk = newUrl[2].startswith('SELECT_PREFIX_TRUE') #ftp
        if flagUrlOk==True:
            print(newUrl[2])
            fileDataName = newUrl[2].split('/') [-1]
            pathFile = savePath+fileDataName
            print(pathFile +'\n')
            urllib.request.urlretrieve( newUrl[2], savePath+fileDataName)