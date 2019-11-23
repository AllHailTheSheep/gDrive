from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

path = input("Folder of .jpgs to upload: ")

ImagePaths = []
for dirpath, dirnames, files in os.walk(path):
    for name in files:
        if name.lower().endswith(".jpg"):
            ImagePaths.append(os.path.join(dirpath, name))
ImagePaths = sorted(ImagePaths)

fid = '1ctheT9uGd-oxl31v1llVqxTRsiefA6eg'
i = 1
for path in ImagePaths:
    f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}], 'title': str(i) + '.jpg'})
    # Make sure to add the path to the file to upload below.
    f.SetContentFile(path)
    f.Upload()
    percentage = round((i/len(ImagePaths)*100), 2)
    print('title: %s, mimeType: %s' % (f['title'], f['mimeType']) + ': ' + str(percentage))
    i += 1
