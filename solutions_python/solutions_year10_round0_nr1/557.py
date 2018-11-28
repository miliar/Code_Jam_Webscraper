import sys
 
def one():
    test = int(sys.stdin.readline().strip())

    for t in xrange(0,test):
        n,k = map(int,sys.stdin.readline().strip().split())

        out = "Case #" + str(t+1) + ":"
        a = 2**n - 1

        if k >= a and (k - a) % (a + 1) == 0:

            print out,"ON"
        else:
            print out,"OFF"

 
one()

