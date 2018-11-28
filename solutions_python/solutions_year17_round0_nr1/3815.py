def flip(s, k, i):
    return s[:i] + [not p for p in s[i:i+k]] + s[i+k:]

def testSolve(s, k):
    nt = sum(p == True for p in s)
    nf = len(s) - nt
    for n in range(len(s)):
        if all(s):
            return n
        counts = list(map(lambda i: sum(p == True for p in s[i:i+k]), range(len(s)-k)))
        print(counts)
        deltas = list(map(lambda i: 2*sum(p == True for p in s[i:i+k])-k, range(len(s)-k)))
        print(deltas, sum(deltas))
        print(s)
        i, _ = min(enumerate(deltas), key=lambda t: t[1])
        print(i)
        s = flip(s, k, i)

def solve(s, k, pos=0, level=0):
    if all(s):
        return level
    nf = sum(p == False for p in s)
    for i in range(pos, len(s)-k+1):
        r = solve(flip(s, k, i), k, i+1, level+1)
        if r:
            return r

def problemA():
    T = int(input())
    for i in range(T):
        s, k = input().split()
        s = [c == '+' for c in s]
        solution = solve(s, int(k))
        print('Case #{}: {}'.format(i+1, solution if solution != None else 'IMPOSSIBLE'))

problemA()
