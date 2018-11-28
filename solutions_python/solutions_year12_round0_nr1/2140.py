myDict = {}


#manual overrdes
#myDict['/n'] = "/n"
myDict['q'] = "z"
myDict['z'] = "q"


s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for i in range(len(s)):
    char = out[i]
    enCrCHar = s[i]
    myDict[enCrCHar] = char

def replace(letter):
    try:
        returnlet = myDict[letter]
    except:
        returnlet = ""
    return returnlet

#numTestCases = int(raw_input())
#for i in range(numTestCases):
    #line = raw_input()
    #newAns = ""
    #for letter in line:
        #newAns += replace(letter)
    #ans = "Case #%d: " % (i+1) + newAns 
    #print ans
        


theFile = open("asmall.txt")
while 1:
    try:
        numTestCases = int(theFile.readline())
    except:
        break
    for i in range(numTestCases):
        line = theFile.readline()
        if not line:
            break
        newAns = ""
        for letter in line:
            newAns += replace(letter)
        ans = "Case #%d: " % (i+1) + newAns 
        print ans
        


