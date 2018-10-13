IN_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-small.in"
OUT_FILENAME = "C:\Users\SONY\SkyDrive\gcj\Quals\A-small-out.txt"
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
    row1=int(base[bind])
    bind+=row1
    nos=base[bind].split()
    bind+=5-row1
    row2=int(base[bind])
    bind+=row2
    no=base[bind].split()
    bind+=5-row2
    isPre=False
    isExt=False
    ans=0
    for i in nos:
        if i in no and not isPre:
            isPre=True
            a=i
        elif i in no:
            isExt=True
            break
    if isExt:
        ans="Bad magician!"
    elif not isPre:
        ans="Volunteer cheated!"
    else:
        ans=str(a)
    print str('Case #'+str(z+1)+': '+ans+'\n')
    outFile.write(str('Case #'+str(z+1)+': '+ans+'\n'))
outFile.close()
'''
input is
base[bind]
bind+=1
'''