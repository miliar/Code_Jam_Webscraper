def perm_given_index(plist, apermindex):
    alist = list(plist)
    for i in range(len(alist)-1):
        apermindex, j = divmod(apermindex, len(alist)-i)
        alist[i], alist[i+j] = alist[i+j], alist[i]
    return alist

def chars(string):
    mylist = []
    for i in range(len(string)):
        mylist.append(string[i])
    return mylist

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def applyPerm(aperm, string):
    out = ""
    for val in aperm:
        i = int(val)
        out = out + string[i]
    return out

def getCompressedLength(string):
    count = 0
    lastchar = ""
    for i in range(len(string)):
        currchar = string[i]
        if (currchar != lastchar):
            count = count + 1
        lastchar = currchar
    return count


f = open("c:/users/roy/Downloads/D-small-attempt0.in")
#f = open("C:/Users/Roy/Documents/gcj/test.in.txt")

nCnt = 0
lines = f.readlines()

#print len(lines)

nCnt = int(lines[0])
#print "There are %i test cases." % nCnt
nCase = 0

nLineNo = 1
for nCase in range(1, nCnt+1):
    #print "Case #%i:" % nCase
    k = int(lines[nLineNo])
    nLineNo = nLineNo + 1
    S = lines[nLineNo].strip()
    nLineNo = nLineNo + 1
    #print "%s : %s" % (k, S)
    basePerm = range(0, k)
    #print basePerm
    minLength = len(S)
    for n in range(factorial(k)):
        currPerm = perm_given_index(basePerm, n)
        #print applyPerm(currPerm, S)
        m = len(S) / k
        chunks = []
        newstr = ""
        for i in range(m):
            chunk = S[i*k:k*(i+1)]
            #chunkl = chars(chunk)
            #chunks.append(chunkl)
            newstr = newstr + applyPerm(currPerm, chunk)
        #print newstr
        newlen = getCompressedLength(newstr)
        if (newlen < minLength):
            minLength = newlen
        
    #print str(chunks)
    count = 0
    print "Case #%i: %i" % (nCase, minLength)
    