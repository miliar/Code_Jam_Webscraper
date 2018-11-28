def isnumber(n):
    try:
        int(n)
        return True
    except:
        ValueError
        return False

def decode(googlerese):
    newgooglerese = ''
    for letter in googlerese:
        if letter != '\n':
            if letter != ' ':
                newgooglerese += codemap[letter]
            else:
                newgooglerese += ' '
    testcases.append(newgooglerese)

codemap = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
testcases = []

f = file("A-small-attempt3.in", "r")

for line in f:
    if isnumber(line) == False:
        decode(line)
f.close()

f1 = file("outputfile.txt", 'w')

for index in range(1,len(testcases)+1):
    f1.write("Case #"+str(index)+': '+testcases[index-1]+'\n')

f1.close()
    