gmap = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def decrypt(caseNumber, caseString):
    out = "Case #%d: " % caseNumber
    for c in caseString:
        out += gmap.get(c, c)
    return out

def readfile(file):
    fp = open(file)
    num = int(fp.readline())
    for i in range(num):
        print(decrypt(i+1, fp.readline().strip()))
    fp.close()
