def memoize(function):
    cache = {}
    def decorated_function(*args):
        try:
            return cache[args]
        except KeyError:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

def solve(n, k):
    if k == 0: return 0, 0
    if k == 1:
        if n % 2 == 1: return (n - 1)//2, (n - 1)//2
        return n//2, (n - 1)//2

    if k % 2 == 0:
        return solve(n//2, k//2)
    else:
        return solve((n - 1)//2, k//2)
solve = memoize(solve)

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        n, k = [int(e) for e in F.readline().split(" ")]
        yield i + 1, n, k

out = open("S.out", "w")

#for (i, n, k) in input("Csample.in"):
#for (i, n, k) in input("C-small-1-attempt1.in"):
#for (i, n, k) in input("C-small-2-attempt0.in"):
for (i, n, k) in input("C-large.in"):
    r = "%d %d" % solve(n, k)
    #print("Case #%d(%d %d): %s" % (i, n, k, r))
    print("Case #%d: %s" % (i, r), file = out)
