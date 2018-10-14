import sys

lang = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}

infile = sys.argv[1]

with open(infile, 'r') as file:
    numlines = int(file.readline())
    for i in range(numlines):
        line = file.readline()
        builder = ""
        for char in line:
            if char in lang.keys():
                builder += lang[char]
            elif (char == "\n"):
                pass
            else:
                builder += char
        print "Case #" + str(i+1) + ": " + builder