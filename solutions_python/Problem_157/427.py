import sys
# sys.stdin = open('in.txt','r')
# sys.stdout = open('out.txt', 'w')

MATRIX = [['','i','j','k'],
          ['i','-','k','-j'],
          ['j','-k','-','i'],
          ['k','j','-i','-']]

MAP = {}
for i,ei in enumerate(['1','i','j','k']):
    for j,ej in enumerate(['1','i','j','k']):
        MAP[ei+ej] = MATRIX[i][j]



def produce(str,target = None,reverse = False):
    sign = 1
    a = ''
    strIter = str
    if reverse:
        strIter = str[::-1]
    for i,c in enumerate(strIter):
        if c=="-":
            sign *= -1
            continue
        if reverse:
            a = c + a
        else:
            a += c
        if len(a)==2:
            a = MAP[a]
        if a[0]=='-':
            sign *= -1
            a = a[1:]
        if target and a == target:
            if reverse:
                remain = str[:len(str)-i-1]
            else:
                remain = str[i+1:]
            if sign>0:
                return remain
            else:
                return '-'+remain
    if target:
        return -1

    if sign == 1:
        return a
    else:
        return '-'+a



def doCase(pattern,X,currentCase):
    flag = 0
    if len(pattern)*X<=10000 or X <= 5:
        ALL = pattern * X
        remain = produce(ALL,'i')
        if remain!=-1:
            remain = produce(remain,'j')
            if remain != -1:
                if produce(remain)=='k':
                    flag = 1
    else:
        start = pattern
        while len(start) < 1000 and X > 1:
            start += pattern
            X -= 1
        remainS = produce(start,'i')
        end = pattern
        while len(end) < 1000 and X > 1:
            end += pattern
            X -= 1
        remainE =  produce(end,'k',True)
        if remainS != -1 and remainE != -1:
            middle = produce(pattern)
            middle *= (X%4)
            if produce(remainS+middle+remainE)=='j':
                flag = 1
    result = "YES" if flag else "NO"
    print "Case #{}: {}".format(currentCase,result)

T = int(sys.stdin.readline())
for i in range(T):
    L, X = sys.stdin.readline().split()
    X = int(X)
    pattern = sys.stdin.readline().strip()
    doCase(pattern,X,i+1)

