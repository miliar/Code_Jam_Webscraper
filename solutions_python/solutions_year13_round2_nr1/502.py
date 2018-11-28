def ngrowths(A, B):
    if A == 1:
        return A, None
    n = 0
    while A <= B:
        A += A - 1
        n += 1
    return A, n

def grow(A, motes):
    nmotes = []
    for m in motes:
        if m < A:
            A += m
        else:
            nmotes.append(m)
    return A, nmotes

def compute(A, motes):
    r = 0
    motes.sort()
    while True:
        A, motes = grow(A, motes)
        if not motes:
            return r
        nA, n = ngrowths(A, motes[0])
        if n is not None and n < len(motes):
            r += n
            A = nA
        else:
            r += len(motes)
            return r
    
def run():
    T = int(raw_input())
    for i in xrange(T):
        A, N = [int(x) for x in raw_input().split()]
        motes = [int(x) for x in raw_input().split()]
        print 'Case #%d:' % (i + 1),
        print compute(A, motes)

if __name__ == '__main__':
    run()
