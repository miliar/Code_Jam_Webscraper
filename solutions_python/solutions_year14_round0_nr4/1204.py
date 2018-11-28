IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\D-small.in"
#OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\D-small-out.txt"
#IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quaals\D-large.in"
OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\D-large-out.txt"
outFile = open(OUT_FILENAME, 'w+' ,0)

def loadWords():
    inFile = open(IN_FILENAME, 'r' , 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList
    
def war(k,n):
    sk=0
    for i in k:
        f=False
        for j in n:
            if float(j) > float (i):
                n.remove(j)
                f=True
                break
        if not f:
            sk+=1
            n.remove(n[0])
    return sk
    
def dwar(k,n):
    sk=0
    k=k[::-1]
    n=n[::-1]
    for i in k:
        for j in n:
            if float (i) > float(j):
                n.remove(j)
                sk+=1
                break
                
    return sk
    
            



base=loadWords()
test=int(base[0])
bind=1
for z in range(test):
    n=base[bind]
    bind+=1
    k=sorted(base[bind].split())
    bind+=1
    n=sorted(base[bind].split())
    bind+=1
    outFile.write(str('Case #'+str(z+1)+': '+str(dwar(k,n))+' '+str(war(k,n))+'\n'))
    print "runned"
outFile.close()
'''
input is
base[bind]
bind+=1
'''