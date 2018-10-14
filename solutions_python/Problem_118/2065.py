import math

f = open('in', 'r')

T = int(f.readline())

def isPalin(n):
    N = str(n)
    while(len(N) > 1):
        if(N[0] != N[len(N) - 1]): return False
        else: N = N[1:(len(N) - 2)]
    return True


for t in range(T):
    line = f.readline().split()
    A = long(line[0])
    B = long(line[1]) 
    count = 0
    for i in range(int(math.ceil(math.sqrt(A))), int(math.ceil(math.sqrt(B + 1)))):
        if isPalin(i) and isPalin(i ** 2):
            count = count + 1
    print "Case #" + str(t + 1 ) + ": " + str(count)

