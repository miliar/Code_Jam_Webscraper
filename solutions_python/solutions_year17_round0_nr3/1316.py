import numpy as np

if __name__ == '__main__':
    t = int(raw_input())
    for i in np.arange(t):
        s = raw_input()
        N, M = [np.uint64(x) for x in s.split(" ")]

        k = int(np.ceil(np.log2(M+1.))-1)   # kth row of tree

        x = np.uint64(np.floor((N-2**k+1.)/2.**k)) # smaller number
        y = x + 1 # larger number
        delta = (N-2**k+1)-2**k*x
        nx = 2**k - delta   # how often does small number occur
        ny = delta # how often the larger number occurs

        # n is the largest number of stalls we like to divide
        if (M-(2**k-1)) <= ny:
            n = y
        else:
            n = x

        if (n-1) % 2 == 0:
            # even
            x = (n-1)//2
            y = (n-1)//2
        else:
            x = (n-1)//2
            y = x + 1

        #print n, np.uint64(n-1), x, y

        print 'Case #%d: ' % (i + 1) + '%d %d' %(int(max(x,y)), int(min(x,y)))