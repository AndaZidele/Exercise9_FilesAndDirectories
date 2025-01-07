import os
import time

print("Please input path of directories!")
correct = False
dirList = []
fileList = []

# /Users/andazidele/Desktop/FolderForPython/python2024/folderForPythonHomeworks

# funkcija kas parbauda vai cels ir direktorija vai fails
# parbauda vai ta nav direktorija, kur, ja ir: iet uz dir. rekurs. parstaigasanas funkc.
# ja nav => tatad tas ir fails => tpc iet uz nakamo funkciju
def checkIfPathIsDirecotry(directoryPath):
    if os.path.isdir(directoryPath):
        dirList.append(os.path.basename(directoryPath))
        traversingDirectories(directoryPath=directoryPath)
    else: 
        fileList.append(os.path.basename(directoryPath))
        getFileInformation(directoryPath=directoryPath)

# funkcija direktoriju rekursivai parstaigasanai:
def traversingDirectories(directoryPath):
    print("[DIR] {}".format(os.path.basename(directoryPath))) # direktorijas nosaukums
    for item in os.listdir(directoryPath):
        item_path = os.path.join(directoryPath, item)  
        checkIfPathIsDirecotry(item_path) # atpakal uz parbaudes funkciju ar nakamo celu


# faila informacijas izdrukasanas funkcija
def getFileInformation(directoryPath):
    print(f"{""}[FILE] {os.path.basename(directoryPath)}") # faila nosaukums
    try:
        file_information = os.stat(directoryPath)
        print("User ID: {}".format(file_information.st_uid))
        print("Creation time: {}".format(time.ctime(file_information.st_ctime)))
        print("Last Access: {}".format(time.ctime(file_information.st_atime)))
        print("Last modified: {}".format(time.ctime(file_information.st_mtime)))
        print("File size: {}".format(file_information.st_size))
        print("File permissions: {}".format(file_information.st_mode))
    except:
        print("Error for getting stats related to this file.")

def listToString(list):
    stringFromList = ""
    for el in list:
        if stringFromList == "":
            stringFromList = el
        else:
            stringFromList = stringFromList + ", " + el
    return stringFromList

# nolasa lietotaja ievadito direktoriju celu un parbauda vai tads eksiste, kur, ja eksiste => iet uz funkciju traversingDirectory
# kamer nav ievadita eksistejosa direktorija, lietotajam tiek prasits to ievadit
while correct==False:
    directoryPath = input()
    if os.path.exists(directoryPath):
            correct = True
            checkIfPathIsDirecotry(directoryPath)
            print("Directory count: {} and file count: {}".format(len(dirList), len(fileList)))
            print("List of directories: {}".format(listToString(dirList)))
            print("List of files: {}".format(listToString(fileList)))
    else:
        print("Directory path does not exists!")
        print("Please input other path of directories!")