import sys

def read():
    global N, M
    global O, E, P
    N, M = [int(x) for x in sys.stdin.readline().split()]
    O = [0] * M
    E = [0] * M
    P = [0] * M
    for i in xrange(M):
        O[i], E[i], P[i] = [int(x) for x in sys.stdin.readline().split()]
        O[i] -= 1
        E[i] -= 1

def cost(x, y, c):
    if x == y:
        return 0
    return (N + N - (y - x - 1)) * (y - x) / 2 * c

def solve(b, x, begin, end):
    while begin < len(b) and b[begin] == 0:
        begin += 1
    while end-1 >= 0 and b[end-1] == 0:
        end -= 1
    if begin >= end:
        return 0
    c = 0
    m = -1
    for i in xrange(begin, end - 1):
        c += b[i]
        if m == -1 or m > c:
            m = c
            mi = i
    
    # print c, m, begin, end, x[begin], x[end-1], cost(x[begin], x[end-1], m)
    # if m == -1:
        # print c, m, begin, end
        # print x
        # print b
    
    b[begin] -= m
    b[end-1] += m
    return cost(x[begin], x[end-1], m) + solve(b, x, begin, mi + 1) + solve(b, x, mi + 1, end)

def work():
    x = sorted(O + E)
    y = []
    for i in xrange(len(x)):
        if i != 0 and x[i-1] == x[i]:
            continue
        y.append(x[i])
    x = y
    del y
    
    index = {}
    for i in xrange(len(x)):
        index[x[i]] = i
    
    b = [0] * len(x)
    for i in xrange(M):
        b[index[O[i]]] += P[i]
        b[index[E[i]]] -= P[i]
    
    m = solve(b, x, 0, len(x))
    
    global Result
    Result = 0
    for i in xrange(M):
        Result += cost(O[i], E[i], P[i])
    
    Result -= m

def write(t):
    sys.stdout.write('Case #{}: {}\n'.format(t, Result))
    
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        read()
        work()
        write( i + 1 )

if __name__ == "__main__":
    main()
