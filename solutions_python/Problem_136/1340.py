import math
inf = open("in.txt", "r")
ouf = open("out.txt","w")

def close_files():
    inf.close()
    ouf.close()

def precount():
        pass

printcounter = 0
def printstr(a):
    global printcounter
    printcounter +=1
    ouf.write('Case #%d: %.7f\n' % (printcounter,a))

def solvetest():
    [c,f,x] = map(float, inf.readline().split())
    gain = 2.0
    mintime = x / gain
    current = 0
    time = mintime
    while current + x/gain <= mintime:
        mintime = current + x/gain
        current += c/gain
        gain += f
    printstr(mintime)
        
precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

