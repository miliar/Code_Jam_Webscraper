import math
def ispal(n):
    return str(n) == str(n)[::-1]

p = [['0','1','2','3','4','5','6','7','8','9'], ['00','11','22','33','44','55','66','77','88','99']]

def genPalin(p, n):
    temp=[]
    for i in range(0,10):
        for j in p[n-2-1]:
            palin = str(i)+str(j)+str(i)
            temp.append(palin)
    p.append(temp)
    #return p

for i in range (3,8):
    genPalin(p,i)

fi = open('C-large-1.in', 'r')
fo = open('C-large-1.out', 'w')
testcases = int(fi.readline())
caseNo = 0
for caseNo in range(1, testcases+1):
    count = 0
    a,b = fi.readline().split()
    a,b = int(a), int(b)
    aSqrt = int(math.ceil(math.sqrt(a)))
    bSqrt =int(math.sqrt(b))
    aLen = len(str(aSqrt))
    bLen = len(str(bSqrt))
    if bLen == 8:
        bLen = 7
    #print aSqrt, aLen, bSqrt, bLen, caseNo
    for i in range(aLen, bLen+1):
        for k in p[i-1]:
            j = int(k)
            if j>=aSqrt and j<=bSqrt:
                if ispal(j*j):
                    count = count + 1
                    if j>bSqrt:
                        break
    #print count
    fo.writelines('Case #'+str(caseNo)+': '+str(count)+chr(10))

