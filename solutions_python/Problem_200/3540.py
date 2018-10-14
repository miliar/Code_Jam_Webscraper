
fin = open('tidy.in','r')
fout = open('tidy.out','w')

def checktidy(n):
    while n > 0:
        start = n % 10
        n /= 10
        nextdig = n % 10
        if nextdig > start:
            return False
    return True

T = int(fin.readline())

for t0 in range(T):
    N = int(fin.readline())
    while not checktidy(N):
        N -= 1
    print N
    fout.write("Case #" + str(t0 + 1) + ": " + str(N) + "\n")

    
