import os, sys

def main():
    fileName = sys.argv[1]

    if fileName[-3:] != ".py":
        return
    
    os.rename(fileName, fileName[:-2] + "bpy")
    fileName = fileName[:-2] + "bpy"

    sourceContent = open(fileName, 'r').read()

    fileContent = ""
    for x in range(len(sourceContent)):
        fileContent += sourceContent[-x - 1]

    with open(fileName, 'w') as file:
        file.write(fileContent)

if __name__ == "__main__":
    main()
