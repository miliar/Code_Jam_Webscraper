import sys, hashlib

fin  = sys.stdin
fout = sys.stdout

def memoize(meth, *args):
    memo = {}
    try:
        return memo[tuple(args)]
    except:
        return memo.setdefault(tuple(args), meth(*args))

def reader():
    while fin:
        yield fin.readline().split(' ')


def dirwalker(dirdict, newdir):
    pass

def main():
    
    T = int(fin.readline())

    for t in xrange(T):
        N, M = map(int, fin.readline().split(' '))

        dirs = {}
        for n in xrange(N):
            ln = fin.readline().strip().split('/')[1:]
##            ln.reverse()
            curr = dirs
            for i in ln:
                curr = curr.setdefault(i, {})

        counter = 0    
        for m in xrange(M):
            ln = fin.readline().strip().split('/')[1:]
            curr = dirs
            for i in ln:
                try:
                    curr = curr[i]
                except:
                    counter +=1
                    curr = curr.setdefault(i, {})
        
        fout.write("Case #%d: %d\n" % (t +1, counter))


if __name__ == '__main__':
    main()
