import sys

def read():
    global N, P
    N, P = [int(x) for x in sys.stdin.readline().split()]

# def best_place(x):
    # p = 0
    # x = 2 ** N - x - 1
    # for i in xrange(N):
        # if x > 0:
            # p = p * 2
            # x = (x - 1) // 2
        # else:
            # p = p * 2 + 1
    # return p

# def worst_place(x):
    # p = 0
    # for i in xrange(N):
        # if x > 0:
            # p = p * 2 + 1
            # x = (x - 1) // 2
        # else:
            # p = p * 2
    # return p

# def work():
    # global Rmin, Rmax
    
    # n2 = 2 ** N
    # for i in xrange(n2):
        # b = best_place(i)
        # w = worst_place(i)
        # print i, b, w
        # if w < P:
            # Rmin = i
        # if b < P:
            # Rmax = i

def work():
    global Rmin, Rmax
    
    p2 = [0] * (N+1)
    for i in xrange(N+1):
        p2[i] = 2 ** i
    
    # Rmax
    Rmax = 0
    x = 0
    p = 0
    for i in xrange(N):
        x += p2[N - i - 1]
        p += p2[i]
        if p < P:
            Rmax = x
    # Rmin
    Rmin = 0
    x = 0
    p = 0
    for i in xrange(N):
        x += p2[i+1]
        p += p2[N-i-1]
        if p < P:
            Rmin = x
            
    if Rmin >= p2[N]:
        Rmin = p2[N] - 1
    if Rmax >= p2[N]:
        Rmax = p2[N] - 1

def write(t):
    sys.stdout.write('Case #{}: {} {}\n'.format(t, Rmin, Rmax))
    
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        read()
        work()
        write( i + 1 )

if __name__ == "__main__":
    main()
