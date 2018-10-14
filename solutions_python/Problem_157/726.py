import sys
import heapq
import math

def printer(thigns):
    for i in thigns:
        sys.stdout.write(str(i))
    print("")

t = int(sys.stdin.readline())

sys.setrecursionlimit(100000)

table = {}
table['1'] = {'1':'1', 'i': 'i', 'j': 'j', 'k': 'k'}
table['i'] = {'1':'i', 'i': '-1', 'j': 'k', 'k': '-j'}
table['j'] = {'1':'j', 'i': '-k', 'j': '-1', 'k': 'i'}
table['k'] = {'1':'k', 'i': 'j', 'j': '-i', 'k': '-1'}


def mult(fst, snd):
    fneg = len(fst) > 1
    sneg = len(snd) > 1
    freal = fst if not fneg else fst[-1]
    sreal = snd if not sneg else snd[-1]
    multvalue = table[freal][sreal]
    multneg = len(multvalue) > 1
    multreal = multvalue if not multneg else multvalue[-1]
    finalneg = fneg ^ sneg ^ multneg
    if finalneg:
        return "-" + multreal
    else:
        return multreal
    

for j in range(t):
    linesplit = sys.stdin.readline().split()
    l = int(linesplit[0])
    x = int(linesplit[1])
    chars = sys.stdin.readline()
    curvalue = '1'
    nextchar = ['i','j','k']
    for k in range(x):
        for i in range(l):
            curvalue = mult(curvalue, chars[i])
            if len(nextchar) > 0:
                if curvalue == nextchar[0]:
                    curvalue = '1'
                    nextchar = nextchar[1:]

    printval = ''
    if len(nextchar) == 0 and curvalue == '1':
        printval = "YES"
    else:
        printval = "NO"

    printer(["Case #", j+ 1, ": ", printval])
    
    
