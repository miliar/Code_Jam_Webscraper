import math
inf = open("in.in", "r")
ouf = open('out.out','w')

def close_files():
        inf.close()
        ouf.close()

def precount():
        pass

printcounter = 0
def printstr(a):
        global printcounter
        printcounter +=1
        print ('Case #%d: %s' % (printcounter,a), file=ouf)

def solvetest():
        n,s = inf.readline().split()
        s = map(int,s)
        friends = 0
        total = 0
        for (i,c) in enumerate(s):
            diff = i - total
            if diff > 0 :
                friends += diff
                total += diff
            total += c
        printstr(friends)
#precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

