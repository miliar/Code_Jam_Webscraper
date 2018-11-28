import sys;
import math;
import operator;
import collections;

class Config:
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return ""
    pass

if __name__ == "__main__":
    n_cases = int(sys.stdin.readline())

    for _i in range(n_cases):
        # Reading...
        result = 0
        N, M = [ int(x) for x in sys.stdin.readline().split() ]
        lawn = []
        for i in xrange(N):
            lawn.append( [int(x) for x in sys.stdin.readline().split()] )

        # Solving...
        max_heights_hor = []
        for i in xrange(N):
            max_heights_hor.append( max( lawn[i] ) )

        max_heights_ver = []
        for i in xrange(M):
            max_heights_ver.append( max( [ x[i] for x in lawn] ) )

        result = "YES"
        for i in xrange(N):
            for j in xrange(M):
                if not (lawn[i][j] == max_heights_hor[i] or lawn[i][j] == max_heights_ver[j]):
                    # it is not posible...
                    result = "NO"
                    break;

        # printing...
        # sys.stderr.write("Case #%s: %s Done!\n"%(_i+1, result))
        print "Case #%s: %s"%(_i+1, result)

