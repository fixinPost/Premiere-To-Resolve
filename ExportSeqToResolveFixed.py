import sys
import os
import time
from os import path
from pathlib import Path

#sys.path.append(r'C:\Users\J\AppData\Local\Programs\Python\Python38\Lib\site-packages\pymiere')
sys.path.append(r'C:\Users\J\AppData\Local\Programs\Python\Python36\Lib\pymiere-master')
import pymiere
sys.path.append(r'C:\Users\J\AppData\Local\Programs\Python\Python36\Lib\pymiere-master\pymiere')
from pymiere import core
from core import eval_script

#CHECK FOR EXPORTS BEFORE EXPORT
savedSet=set()
myPath = r'C:\Users\J\Desktop\mb testing 21\premiere to resolve\export folder' 



#eval_script(filepath = r'C:\Users\J\Desktop\mb testing 21\premiere to resolve\exportSeqByPreset.jsx')

eval_script("var myPre = 'C:\\Users\\J\\Documents\\Adobe\\Adobe Media Encoder\\14.0\\Presets\\premiereToResolve.epr'")
eval_script('app.enableQE()')
eval_script("app.encoder.encodeSequence(app.project.activeSequence, 'C:\\Users\\J\\Desktop\\mb testing 21\\premiere to resolve\\export folder\\ ' + app.project.activeSequence.name.toString(), myPre, 1, 0)")
eval_script('app.encoder.startBatch()')
activeSeq = str(pymiere.objects.app.project.activeSequence.name)


#CHECK FOR OUR EXPORT AFTER IT'S RENDERED
#print(os.listdir(myPath))

nameSet=set()
for file in os.listdir(myPath):
    fullpath=os.path.join(myPath, file)
    if os.path.isfile(fullpath):
        nameSet.add(file)
print(nameSet)

oldLength = (len([name for name in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, name))]))
oldDir = os.listdir(myPath)
while oldLength == oldLength:
    print('not done')
    for file in os.listdir(myPath):
        fullpath=os.path.join(myPath, file)
    if os.path.isfile(fullpath):
        nameSet.add(file)
    print(len(nameSet))
    if len(nameSet) > oldLength:
        break

newDir = (os.listdir(myPath))
print(oldDir)
print(newDir)

for i in oldDir[:]:
    if i in newDir:
        newDir.remove(i)
print(newDir)

ml = []
for idx, string   in enumerate(newDir):
    if 'm4v' in string:
        print('found m4v')
        ml.append(idx)
    if 'aac' in string:
        print ('found aac')
        ml.append(idx)
    if 'tmp' in string:
        print('yo')
        ml.append(idx)
    #if 'tmp' in string:
       # print('found temp')
        #del string
print (ml)
ml = ml[::-1]
print(ml)
#del newDir[0]
print(newDir)
for idx, val in enumerate(ml):
    del newDir[val]

print(newDir)
myVid = os.path.join(myPath, newDir[0])
print(os.path.exists(myVid))



#YOU DID IT! NOW IMPORT IT INTO RESOLVE
file1 = open("myfile.txt","w")

file1.write("Hello \n")
import DaVinciResolveScript as dvr_script
resolve = dvr_script.scriptapp("Resolve")
fusion = resolve.Fusion()
#print(fusion, ' is fusion.')
projectManager = resolve.GetProjectManager()
proj = projectManager.GetCurrentProject()
mediaStorage = resolve.GetMediaStorage()
mp = proj.GetMediaPool()
root = mp.GetRootFolder()
root_subs = root.GetSubFolders()
print(mp)
ml = [r'C:\Users\J\Desktop\mb testing 21\premiere to resolve\export folder\ mySeq_2.mp4']
print(mediaStorage)
print(mediaStorage.GetMountedVolumeList())
#mediaStorage.AddItemListToMediaPool(ml[1])
print(myVid)
ml = os.listdir(myPath)
print(ml)
yo = "C:/Users/J/Desktop/mb testing 21/premiere to resolve/export folder/ mySeq.mp4"
mediaStorage.AddItemListToMediaPool(r'C:\Users\J\Desktop\mb testing 21\premiere to resolve\export folder\ mySeq.mp4') 
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
print(mediaStorage.AddItemListToMediaPool(ml[0]))
time.sleep(4)
ml = os.listdir(myPath)
#mediaStorage.AddItemListToMediaPool(ml[0])
mediaStorage.AddItemListToMediaPool(myVid)
print(ml[0])
print(myVid)
# \n is placed to indicate EOL (End of Line)
#file1.write(myVid)
#file1.writelines(L)
#file1.close() 
#import writeToFile



