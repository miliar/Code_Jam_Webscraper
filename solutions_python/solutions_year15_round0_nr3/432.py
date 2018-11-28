fin = open("input.txt", "r")
fout = open("output.txt", "w")

def mul(x, y):
    flag = 1 if (x > 0) ^ (y > 0) == 0 else -1
    return flag * _mul[abs(x) - 1][abs(y) - 1]

_mul = [
[1, 2, 3, 4],
[2, -1, 4, -3],
[3, -4, -1, 2],
[4, 3, -2, -1]
]

ttt = {'i' : 2, 'j' : 3, 'k' : 4}

def solve():
    L, X = map(int, fin.readline().split())
    s = [ttt[x] for x in fin.readline().strip('\n')] * X
    n = L * X
    tail = n * [0]
    for i in xrange(n - 1, -1, -1):
        tail[i] = mul(s[i], tail[i + 1]) if i != n - 1 else s[i]
    a = 1
    for i in xrange(n):
        a = mul(a, s[i])
        if a == 2:
            b = 1
            for j in xrange(i + 1, n - 1):
                b = mul(b, s[j])
                if b == 3 and tail[j + 1] == 4:
                    return "YES"
    return "NO"

T = int(fin.readline())

for _ in xrange(T):
    print >> fout, "Case #%d: %s" % (_ + 1, solve())
    

fin.close()
fout.close()
