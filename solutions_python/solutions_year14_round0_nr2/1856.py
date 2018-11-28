import sys

def ans(C, F, X):
    s = [[2, 0, 1]]
    def _ans(v, sec, n):
        a = sec + X/v
        b = sec + C/v + X/(v+F)
        if a < b or C*n>X:
            return a

        s.append([v+F, sec+C/v, n+1])
        return None

    while s:
        a = _ans(*s.pop())
        if a: return a

    return '!'


with open(sys.argv[1]) as fr, open('b.out', 'w') as fw:
    T = int(fr.readline())
    for i in xrange(T):
        no = i + 1
        (C, F, X) = map(float, fr.readline().split(' '))
        fw.write("Case #{no}: {ans:1.7f}\n".format(no=no,ans=ans(C, F, X)))

