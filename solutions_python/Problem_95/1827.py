file = open("sample")

trans = {'z': 'q', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', '\n':'', ' ':' '}

def translate(line):
    l = list(line)
    for index, char in enumerate(l):
        l[index] = trans[char]
    return ''.join(l)

lineNo = 0
while 1:
    line = file.readline()
    if not line:
        break
    pass
    if lineNo == 0:
        testCount = line
    else:
        print 'Case #' + str(lineNo) + ': ' + translate(line)
    lineNo = lineNo + 1

