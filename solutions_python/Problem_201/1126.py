def readFile(fileName=""):
    while True:
        try:
            if fileName == "":
                fileName = input("Enter file name: ")
            file = open(fileName, "r")
            break
        except FileNotFoundError:
            print ("Invalid file name!")
            fileName = ""

    return file

def fileContents(file, f):
    contents = [f(line) for line in file]
    file.close()
    return contents

def readToContents(f, fileName=""):
    return fileContents(readFile(fileName), f)

def toInt(string):
    try:
        return int(string.replace("\n",""))
    except ValueError:
        print ("Error parsing to string")
        return ""

def readInts(fileName=""):
    return readToContents(toInt, fileName)

def writeFile(contents, f, fileName=""):
    if fileName == "":
        fileName = input("Enter file name: ")

    file = open(fileName, "w")
    i = 0
    for line in contents:
        i += 1
        print (f(line, i), file=file)
    return

def syntax(line, i):
    return ("Case #%s: %s" % (i, line))

if __name__ == "__main__":
    print(readToContents(toInt))
    
