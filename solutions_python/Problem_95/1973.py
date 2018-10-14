# Google Dictionary
GoogDict = {'\n':'\n', 'z':'q', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
"""
The following is simply to build the dictionary from given strings
"""
# Test Strings
Case1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
Case2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
Case3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

# English Translations
Case1Trans = "our language is impossible to understand"
Case2Trans = "there are twenty six factorial possibilities"
Case3Trans = "so it is okay if you want to just give up"

def buildDict(string, translation):
    for i in range(len(string)):
        char = string[i]
        if not (char in GoogDict): GoogDict[char] = translation[i]
        else:
            if GoogDict[char] != translation[i]:
                print "ERROR"
                print char, GoogDict[char], translation[i]
    print GoogDict
""""""""""""""""""""""""

def translate(string):
    newString = ""
    for c in string:
        newString+= GoogDict[c.lower()]
    return newString


"""
The following reads in from input file
"""
fileName = raw_input("Please input the filename of input ")
f = open(fileName, 'r+')
""""""""""""
T = int(f.readline())

"""
And this generates output and writes to file
"""
output = ""
for n in range(1,T+1):
    output+="Case #" + str(n) + ": " + translate(f.readline())
print output
f.close()

g = open(fileName[:fileName.index('.')]+"_output"+
         fileName[fileName.index('.'):], "r+")
g.write(output)
