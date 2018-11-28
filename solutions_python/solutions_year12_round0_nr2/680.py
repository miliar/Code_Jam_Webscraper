import math
inf = open("in.txt", "r")
ouf = open('out.txt','w')

def close_files():
        inf.close
        ouf.close

def precount():
        pass

printcounter = 0
def printstr(s):
        global printcounter
        printcounter +=1
        print >>ouf, 'Case #%d: %s' % (printcounter, s)
        #print >> ouf, st
        #print st

def add(a,b):
        return a + float(b)

def solvetest():
        inp = map(int, inf.readline().split())
        n,s,p = inp[0:3]
        a = inp[3:]
        #print n,s,p,a
        count = 0
        if p == 0:
                count = n
        elif p == 1:
                for i in a:
                        if i>=1:
                                count +=1
        else:
                for i in a:
                        if i>=p*3-2:
                                count += 1
                        elif (i>=p*3-4) and (s>0):
                                count += 1
                                s -= 1
        #print count
        printstr(count)
precount()
testnum = int(inf.readline())
for test in xrange(testnum):
        solvetest()
close_files()
