
import sys

def find_best(L, Q, s, e):
    """ Find the engine which is able to process all queries up to the highest index
    @param L list of engines
    @param Q list of queries
    @param s: start index
    @param e: end index
    @return index of next query to process """
    i = -1
    for E in L:
        try:
            I = Q.index(E, s, e)
        except ValueError:
            return e
        else:
            i = max(i, I)
    return i

def count_switches(L, Q):
    """ Count the swithes needed to process the queries
    @param L list of engines
    @param Q list of queries
    @return number f switches """
    i = 0
    n = len(Q)
    s = 0
    i = find_best(L, Q, i, n)
    while i < n:
        s += 1
        i = find_best(L, Q, i, n)
    return s

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: %s <input> <output>" % sys.argv[0]
        sys.exit()
    fd = open(sys.argv[1], 'r')
    fd2 = open(sys.argv[2], 'w')
    n = int(fd.readline())
    for i in xrange(n):
        N = int(fd.readline())
        L = [fd.readline().strip() for j in xrange(N)]
        N = int(fd.readline())
        Q = [fd.readline().strip() for j in xrange(N)]
        x = count_switches(L, Q)
        fd2.write("Case #%i: %s\n" % (i + 1, x))
    fd.close()
    fd2.close()
