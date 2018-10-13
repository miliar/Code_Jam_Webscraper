IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\B-small.in"
#OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\B-small-out.txt"
#IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quaals\B-large.in"
OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\B-large-out.txt"
outFile = open(OUT_FILENAME, 'w+' ,0)

def loadWords():
    inFile = open(IN_FILENAME, 'r' , 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList

#def comp(c,f,x):
    
base=loadWords()
test=int(base[0])
bind=1
for z in range(test):
    line=str(base[bind])
    bind+=1
    line=line.split()
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    init=2
    t=0;t1=1;t2=0
    while min(t1,t2)==t2:
        t1=t + x/init
        t2=t + c/init + x/(init+f)
        t += c/init
        init=init+f
    print str('Case #'+str(z+1)+': '+str(t1)+'\n')
    outFile.write(str('Case #'+str(z+1)+': '+str(t1)+'\n'))
outFile.close()
'''
input is
base[bind]
bind+=1
'''