'''
Created on 13 Apr 2013

@author: mengda
'''

def process(A, N, I, motes):
    rlt = 0
    
    if A == 1:
        return N
    
    for i in range(I, N):
        if motes[i] < A:
            A += motes[i]
        else:
            #if motes[i] >= A * 2 ** (N - i):
            #    return N - i
            tmp = A * 2 - 1
            if motes[i] < tmp:
                A = tmp + motes[i]
                rlt += 1
            else:
                tmp1 = process(tmp, N, i, motes) + 1
                tmp2 = process(A, N, i + 1, motes) + 1
                rlt += min(tmp1, tmp2)
                break
    return rlt

f = open('A-small-attempt4.in', 'r')
#f = open('1B_A_t.in', 'r')
T = int(f.readline())
outLine = []

for i in range(1, T + 1):
    (A, N) = map(int, f.readline().split())
    motes = map(int, f.readline().split())
    motes = sorted(motes)
    outLine.append('Case #%d: %s\n' % (i, process(A, N, 0, motes)))
    print outLine[-1],

f.close()
outFile = open('1B_A_s4.out', 'w')
outFile.writelines(outLine)
outFile.close()

