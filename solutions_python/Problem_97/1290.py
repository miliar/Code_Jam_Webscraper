import sys

def between(A, B, n, m):
    return A <= n < m <= B

def barrel(s, n):
    return s[n:] + s[:n]

def check(A, B):
    length = len(A)
    A, B = int(A), int(B)
    checked = set()
    for n in range(A, B):
        for i in range(length):
            m = int(barrel(str(n), i))
            if between(A, B, n, m):
                checked.add( (n,m) )
    return len(checked)


with open(sys.argv[1]) as r:
    data = r.read().split('\n')[1:]

data = [l.split(' ') for l in data if l]

with open('out.txt', 'wb') as w:
    for i, pair in enumerate(data):
        w.write('Case #%d: %d\n' % (i+1, check(*pair) ) )

