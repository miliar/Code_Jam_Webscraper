import math
inf = open("in.txt", "r")
ouf = open("out.txt","w")

def close_files():
    inf.close()
    ouf.close()

def precount():
        pass

printcounter = 0
def printstr(a, b):
    global printcounter
    printcounter +=1
    ouf.write('Case #%d: %d %d\n' % (printcounter, a, b))

def solvetest():
    n = int(inf.readline())
    na = list(map(float, inf.readline().split()))
    na.sort()
    ke = list(map(float, inf.readline().split()))
    ke.sort()
    swar = 0
    nak = 0
    kek = 0
    while nak < n and kek<n:
        if na[nak]>ke[kek]:
            swar += 1
            nak += 1
            kek += 1
        else:
          nak += 1  
    war = 0
    nak = 0
    kek = 0
    while kek<n:
        if na[nak]<ke[kek]:
            nak += 1
            kek += 1
        else:
            kek += 1
            war += 1
   
    printstr(swar, war)
        
precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

