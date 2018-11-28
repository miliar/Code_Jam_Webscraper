import sys
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: standing-ovation.py <inputfile>")
        sys.exit()
    try:
        inputFile = open(sys.argv[1], "rU")
    except:
        print("File not found.")
        sys.exit()
    outputFile = open('output.out', "w")
    #list of lines
    fileContent = inputFile.readlines()
    times = fileContent.pop(0)
    for i in range(int(times)):
        line = fileContent[i].split()
        maxShy = line[0]
        total = 0
        needed = 0
        friends = 0
        for person in line[1]:
            needed += 1
            total += int(person)
            if total < needed:
                total += 1
                friends += 1
        outputFile.write("Case #" + str((i+1)) + ": " + str(friends) + '\n')

    
if __name__ == "__main__":
    main()
