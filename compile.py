import sys

def main():
    fileName = sys.argv[1]

    if fileName[-4:] != ".bpy":
        return

    sourceContent = open(fileName, 'r').read()

    fileContent = ""
    for x in range(len(sourceContent)):
        fileContent += sourceContent[-x - 1]

    exec(fileContent)

if __name__ == "__main__":
    main()
