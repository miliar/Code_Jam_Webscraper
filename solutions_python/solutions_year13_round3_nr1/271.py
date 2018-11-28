'''
Created on Oct 15, 2012

@author: mengda
'''

def process(S, n):
    rlt = 0
    L = len(S)
    s = []
    for i in S:
        if i in 'aeiou':
            s.append(0)
        else:
            s.append(1)
    tmp = 0
    for i in range(L):
        s[i] = s[i] * tmp + s[i]
        tmp = s[i]
    for i in range(L):
        idx = i + n - 1
        while(idx < L):
            if s[idx] >= n:
                rlt += L - idx
                break
            idx += 1
    return rlt

f = open('A-small-attempt0.in', 'r')
# f = open('1B_B_t.in', 'r')
T = int(f.readline())
outLine = []

for i in range(1, T + 1):
    (S, n) = f.readline().split()
    outLine.append('Case #%d: %s\n' % (i, process(S, int(n))))
    print outLine[-1],

f.close()
outFile = open('A.out', 'w')
outFile.writelines(outLine)
outFile.close()
