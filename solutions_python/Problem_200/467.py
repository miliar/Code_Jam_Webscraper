import sys



def foo2(n, a):
    if len(n) == 1:
        if n[0] >= a:
            return n[:]
        else:
            return None

    if n[0] > a:
        res1 = foo2(n[1:], n[0])
        if res1 is not None:
            return [n[0]] + res1
        return [n[0]-1] + [9]*(len(n)-1)

    if n[0] == a:
        res1 = foo2(n[1:], n[0])
        if res1 is not None:
            return [n[0]] + res1
        return None

    if n[0] < a:
        return None        




def foo(ifile):
    n = [int(x) for x in ifile.readline().strip()]
    res = foo2(n, 0)    
    res2 = 0
    for x in res:
        res2 = res2 * 10 +x
    return res2


def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

