
__author__ = 'sergeyy'
import time


def check(first, fMat, second, sMat):
    a = fMat[first]
    b = sMat[second]
    fLine = set(fMat[first])
    sLine = set(sMat[second])
    n = fLine&sLine

    if len(n) == 1:
        return str(n.pop())
    elif len(n) == 0:
        return "Volunteer cheated!"
    elif len(n)>1:
        return "Bad magician!"

case = 1
fMat = [[]*4]*4
sMat = [[]*4]*4
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            fMat = [[],[],[],[]]
            sMat = [[],[],[],[]]
            first = int(fin.readline())
            for j in range(4):
                l = fin.readline()
                for c in l[:-1:].split(' '):
                    fMat[j].append(int(c))

            second = int(fin.readline())
            for j in range(4):
                l = fin.readline()
                for c in l[:-1:].split(' '):
                    sMat[j].append(int(c))

            oline = ''
            oline = 'Case #' + str(i) +': ' + check(first-1, fMat, second-1, sMat) +'\n'
            fout.write(oline)
            #fin.readline()
#print (time.clock())



