#!/usr/bin/python3

import os
import json
from playsound import playsound

data = []

#create json file
def createJson(answer):
    print(files +  '------- ' + answer)
    newJson = '{}'
    newData = {files:answer}
    objectPy = json.loads(newJson)
    objectPy.update(newData)
    updateJson = (json.dumps(objectPy))
    data.append(updateJson)
    with open('data.json', 'w') as file:
        json.dump(data, file)

#get a path
print("Please specify audio file directory absolute path:\nExample --'/home/saro/task/audio' ")

path = input()

#checking the directory
if os.path.exists(path) and os.listdir(path):

    folder=os.listdir(path)

    for files in folder:
        if files.endswith(".mp3") or files.endswith(".wav"):
            #play the audio file
            playsound(path + "/" + files)

            print("Press 'c' if the audio is clear and 'n' if there are noises")
            answer = input()

            if answer == 'c' or answer == 'n':
                createJson(answer)
            else:
                print("You need to choose 'c' or 'n' ")
                answer = input()
                if answer == 'c' or answer == 'n':
                    createJson(answer)
                else:
                    exit("Try to run the script again")
        else:
            print("The file is not audio")
else:
    print("Your specified path does not exist or audio file directory is empty")
