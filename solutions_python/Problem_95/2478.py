print "Enter file name."
filename = raw_input()
inFile = open(filename, 'r')
outFile = open('output', 'w')
langDict = {'a' : 'y', 'b' : 'h', 'c' : 'e', 'd' : 's', 'e' : 'o', 'f': 'c', 'g' : 'v', 'h' : 'x', 'i' : 'd', 'j' : 'u',
'k' : 'i', 'l' : 'g', 'm' : 'l', 'n' : 'b', 'o' : 'k', 'p' : 'r', 'q' : 'z', 'r' : 't', 's' : 'n', 't' : 'w', 'u' : 'j',
'v' : 'p', 'w' : 'f', 'x' : 'm', 'y' : 'a', 'z' : 'q'}

def translate(line):
    translation = ""
    linez = line.split()
    for word in linez:
        for char in word:
            translation = translation + langDict[char]
        translation = translation + ' '

    return translation

cases = inFile.readline()

counter = 1
for line in inFile:
    outFile.write("Case #" + str(counter) + ': ' + translate(line) + '\n')
    counter += 1