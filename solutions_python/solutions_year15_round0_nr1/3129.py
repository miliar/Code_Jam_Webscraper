IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-small.in"
#OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-small-out.txt"
#IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quaals\A-large.in"
OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-large-out.txt"
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
    line = base[z+1]
    line = line.split(' ');
    print line
    su = 0
    req=0
    su=int(line[1][0])
    for i in range(1,len(line[1])):
        a = line[1][i]
        print su
        if(su<=i):
             req = req - su + i
             su = i
        su= su + int(a)
        
        
    outFile.write(str('Case #'+str(z+1)+': '+str(req)+'\n'))
outFile.close()
'''
input is
base[bind]
bind+=1
'''