import math
from bisect import bisect_left, bisect_right

list_n = []

def check(n1):
    n2 = n1 * n1
    sq = str(n2)
    d1 = len(sq)
    for i in range(d1/2):
        if (sq[i] != sq[d1 - 1 - i]):
             return
    list_n.append(n2)
    
def loop(n, nu):
    if (n < 0):
        nu1 = int(nu + nu[s::-1])
        check(nu1)
        return
    
    for i in range(10):
        loop(n-1, nu + str(i))

for t in range(1, 4):
    list_n.append(t*t)

for t in range(2, 15):
    print t
    d = int(math.ceil(t/2.))
    s = -(t % 2) - 1
    for i in range(1, 10):
        loop(d-2, str(i))

def GetNumber(n1, n2):
    p1 = bisect_left(list_n, n1)
    p2 = bisect_right(list_n, n2)
    return p2 - p1

fin = open("c:\\jam\\input.in", 'r')
fout = open("c:\\jam\\output", "w")
i = -1
for line in fin.readlines():
    i += 1
    if (i == 0): 
        continue
    fields = line.split(" ")
    (A,B) = int(fields[0]), int(fields[1])
    print >> fout, "Case #%i: %i" % (i, GetNumber(A, B))
	
fout.close()