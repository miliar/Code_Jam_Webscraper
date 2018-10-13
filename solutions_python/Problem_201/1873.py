import sys
read = lambda f=int: map(f, sys.stdin.readline().split())
def calc(i, xs):
    L = xs[:i][::-1].index(1)
    R = xs[i:].index(1)-1
    #print('calc', i, L, R)
    return min(L, R), max(L, R)

def solve(xs, k):
    for _ in range(k):
        best = (-10**10,)*3
        for i, x in enumerate(xs):
            if x == 0:
                mi, ma = calc(i, xs)
                best = max(best, (mi, ma, -i))
        mi, ma, i = best
        #print(mi, ma, -i)
        xs[-i] = 1
        #print(xs)
    return mi, ma

#n = int(sys.argv[1])
#solve([1]+[0]*n+[1], n)

T, = read()
for case in range(T):
    n, k = read()
    xs = [1]+[0]*n+[1]
    mi, ma = solve(xs, k)
    print('Case #{}: {} {}'.format(case+1, ma, mi))

