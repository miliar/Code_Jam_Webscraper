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
    ouf.write('Case #%d: %s\n' % (printcounter,a))

def solvetest():
    n1 = int(inf.readline())
    inp1 = [list(map(int, inf.readline().split()))for x in range(4)]
    ans1 = set(inp1[n1-1])
    n2 = int(inf.readline())
    inp2 = [list(map(int, inf.readline().split()))for x in range(4)]
    ans2 = set(inp2[n2-1])
    ans = ans1 & ans2
    if len(ans) == 1:
        printstr(str(list(ans)[0]))
    elif len(ans) == 0:
        printstr("Volunteer cheated!")
    else:
        printstr("Bad magician!")
precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

