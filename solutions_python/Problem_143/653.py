IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\B-small.in"
OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\B-small-out.txt"
#IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quaals\A-large.in"
#OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-large-out.txt"
outFile = open(OUT_FILENAME, 'w+' ,0)

def loadWords():
    inFile = open(IN_FILENAME, 'r' , 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList

base=loadWords()
test=int(base[0])
bind=1
for z in range(test):
    l = base[bind]
    bind+=1
    a,b,k=l.split()
    
    ctr=0
    for i in range(int(a)):
        for j in range(int(b)):
            if i & j< int(k):
                ctr+=1
                
    
    print str('Case #'+str(z+1)+': '+str(ctr)+'\n')
    outFile.write(str('Case #'+str(z+1)+': '+str(ctr)+'\n'))
outFile.close()
'''
input is
base[bind]
bind+=1
'''