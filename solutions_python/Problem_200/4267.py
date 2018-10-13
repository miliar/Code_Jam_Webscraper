'''
def getTidyListOf(L):
    if len(L) > 1:
        if L[0] > L[1]:
            L[1] = 9
            L[0] -= 1
        tmp = getTidyListOf(L[1:])
        if L[0] > tmp[0]:
            tmp[0] = 9
            L[0] -= 1
        L = [L[0]] + tmp
    return L

def getLastTidy(a):
    L = getTidyListOf([int(x) for x in str(a)])
    return int(''.join(map(str,L)))
'''

def isTidy(a):
    L = [int(x) for x in str(a)]
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

def getLastTidy(a):
    for i in range(a, -1, -1):
        if isTidy(i):
            return i

t = int(raw_input())
for i in xrange(1, t+1):
    a = int(raw_input())
    print("Case #" + str(i) + ": " + str(getLastTidy(a)))

