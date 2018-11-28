fin = open("A-large.in")
fout = open("output.txt", 'w')

def f(n, s):
    n = int(n)
    A = list(map(int, list(s)))
    ans = 0
    claps = 0
    n = len(A)
    for i in range(n):
        if claps < i:
            x = i - claps
            ans += x
            claps += x
        claps += A[i]
    return ans


t = int(fin.readline())
for case in range(t):
    n, s = fin.readline().split()
    ans = f(n, s)
    print("Case #%i: %i" % (case + 1, ans), file = fout)

fin.close()
fout.close()