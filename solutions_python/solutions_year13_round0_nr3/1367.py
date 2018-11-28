import math

def isPalin(n):
    L = []
    while (n>0):
        L.append(n%10)
        n = n/10
    for i in range(len(L)/2):
        if (L[i]!=L[len(L)-1-i]):
            return False
    return True

#infile = open('C.in', 'r')
#outfile = open('C.out', 'w')

infile = open('C-small-attempt0.in', 'r')
outfile = open('C-small-attempt0.out', 'w')

T = int(infile.readline())
#print T
for t in range(1, T+1):
    line = infile.readline()
    parts = line.split()
    A = int(parts[0])
    B = int(parts[1])
    a = int(math.sqrt(A))
    b = int(math.sqrt(B))
    if (a*a !=A):
        a+=1
    cnt =0
    #print a, b,
    for n in range(a, b+1):
        if isPalin(n*n) and isPalin(n):
            cnt+=1
    #print 'Case #'+str(t)+': '+str(cnt)
    outfile.write('Case #'+str(t)+': '+str(cnt)+'\n')
outfile.close()
