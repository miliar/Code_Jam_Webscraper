
def k_subsets_i(n, k):
    '''
    Yield each subset of size k from the set of intergers 0 .. n - 1
    n -- an integer > 0
    k -- an integer > 0
    '''
    # Validate args
    if n < 0:
        raise ValueError('n must be > 0, got n=%d' % n)
    if k < 0:
        raise ValueError('k must be > 0, got k=%d' % k)
    # check base cases
    if k == 0 or n < k:
        yield set()
    elif n == k:
        yield set(range(n))

    else:
        # Use recursive formula based on binomial coeffecients:
        # choose(n, k) = choose(n - 1, k - 1) + choose(n - 1, k)
        for s in k_subsets_i(n - 1, k - 1):
            s.add(n - 1)
            yield s
        for s in k_subsets_i(n - 1, k):
            yield s

def k_subsets(s, k):
    '''
    Yield all subsets of size k from set (or list) s
    s -- a set or list (any iterable will suffice)
    k -- an integer > 0
    '''
    s = list(s)
    n = len(s)
    for k_set in k_subsets_i(n, k):
        yield set([s[i] for i in k_set])


def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')
    n = int(ifile.readline())
    for i in range(0, n):
        n, A, B, C, D, x0, y0, M = map(int, ifile.readline().split(' '))
        #print n, A, B, C,D, x0, y0, M

        X, Y = x0, y0
        #print X, Y
        v = [(x0, y0)]
        for j in xrange(0, n-1):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            v.append((X, Y))
            #print X, Y
        v1 = list(k_subsets(v, 3))
        cnt = 0
        print v
        for a in v1:
            l = list(a)
           # print l
            x = divmod(l[0][0] + l[1][0] + l[2][0], 3)
            y = divmod(l[0][1] + l[1][1] + l[2][1], 3) 
            #print x, y
            if x[1] == 0 and y[1] == 0:
                    cnt +=1
        #print cnt
        ofile.write('Case #%i: %i' %(i+1,cnt))
        if i != (n - 1):
            ofile.write('\n')
        
    ofile.close()
    print 'done'

if __name__ == '__main__':
  main()