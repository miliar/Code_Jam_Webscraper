import sys

fin  = sys.stdin
fout = sys.stdout

def memoize(meth, *args):
    memo = {}
    def f(*args):
        try:
            return memo[tuple(args)]
        except:
            return memo.setdefault(tuple(args), meth(*args))
    return f
def reader():
    return fin.readline().split(' ')


def main():
    T = int(reader()[0])

    for t in xrange(T):
        N = int(reader()[0])

        a, b, counter = {}, {}, 0
        for n in xrange(N):
            w = map(int, reader())
            a.setdefault(w[0], w[1])
            b.setdefault(w[1], w[0])

        ak = a.keys()
        ak.sort()
        bk = b.keys()
        bk.sort()
        
        for i in ak:
            for k in bk:
                if (k < a[i]) and (b[k] > i):
                    counter += 1
                    
        fout.write("Case #%d: %d\n" % (t +1, counter))


if __name__ == '__main__':
    main()
