'''
Created on Apr 7, 2017

@author: Vicki
'''


def keepGoing(current, length):
    for i in range(1,length):
        if int(current[i]) < int(current[i-1]):
            return i-1
    return -1


def lastTidy(num):
    if len(str(num))==1:
        return num
    zahl = str(num)
    while(True):
        if keepGoing(zahl, len(zahl)) == -1: #done
            return int(zahl)
        ind = keepGoing(zahl, len(zahl))
        untidyNums = zahl[ind:]
        tidiedNums = str(int(untidyNums[0])-1) + "9"*(len(untidyNums)-1)
        zahl = zahl[:ind] + tidiedNums
        
        
def readFile(fname):
    f = open(fname)
    liste = []
    for line in f:
        liste.append(line.strip())
    f.close()
    return liste


fileAsList = readFile("B-large.txt")
t = int(fileAsList[0])
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, lastTidy(int(fileAsList[i]))))  