
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %d\n'%(i+1,l))


def getToken(token):
    isToken = False
    ls = []
    s = token
    
    for c in s:
        if c=='(':
            ls.append( [] )
            isToken = True
        elif c==')':
            isToken = False
        else:
            if isToken:
                ls[-1].append(c)
            else:
                ls.append([c])
    print len(ls),ls
    return ls

f = open('Large.in')
contents = f.readlines()
s =contents[0].split()
nLength = int(s[0])
nWords = int(s[1])
nTokens = int(s[2])
print nWords
print nTokens
dWords = {}
lsResult = []
for i in range(1,1+nWords):
    #print 'words:',contents[i]
    word = contents[i].strip()
    for i in range(1,len(word)+1):
        dWords[word[:i]]=1
for i in range(1+nWords,1+nWords+nTokens):
    #print 'token:',contents[i]
    count = 0
    ts = getToken(contents[i].strip())
    ls = [[]]
    for r in ts:
        #print 'r:',r
        lsTemp = []
        for l in ls:
            word = ''.join(l)
            for c in r:
                #print word+c
                if dWords.get(word+c):
                    #print 'true'
                    lt = l[:]
                    lt.append(c)
                    lsTemp.append(lt)
                    #print lsTemp
                    #print ls
        ls = lsTemp
                    
    lsResult.append(len([l for l in ls if l]))
    
    print '\n\n\n\n'
    

#print lsResult
    
wf('x.out',lsResult)