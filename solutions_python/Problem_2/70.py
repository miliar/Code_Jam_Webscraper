
import sys

def conv_hr(x):
    """ Convert time (hh:mm) to minutes """
    return 60*int(x[:2]) + int(x[3:])

def find_next(a, t, T):
    """ Find next train
    @param a Arrival time
    @param t Turnaround time
    @param T List of trains, sorted by arrival time (and departure time if equal)
    @return index or None """
    d = a + t
    for i, x in enumerate(T):
        if x[0] >= d:
            return i
    return None

def key1(t):
    return 3600*t[1] + t[0]

def solve(A, B, t):
    """ Solve the problem
    @param A List of trains starting from station A
    @param B List of trains starting from station B
    @param t Turnaround time
    @return (count at A, count at B)"""
    A.sort(key=key1)
    B.sort(key=key1)
    c = [0, 0]
    k = 0
    while len(A) > 0 and len(B) > 0:
        if A[0][1] > B[0][1]:
            A, B = B, A
            k = 1 - k
        c[k] += 1
        a = A[0][1]
        del A[0]
        i = find_next(a, t, B)
        while i != None:
            a = B[i][1]
            del B[i]
            A, B = B, A
            k = 1 - k
            i = find_next(a, t, B)
    if len(A) == 0:
        A, B = B, A
        k = 1 - k
    if len(A) > 0:
        c[k] += len(A)
    return c

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: %s <input> <output>" % sys.argv[0]
        sys.exit()
    fd = open(sys.argv[1], 'r')
    fd2 = open(sys.argv[2], 'w')
    n = int(fd.readline())
    for i in xrange(n):
        t = int(fd.readline())
        na, nb = map(int, fd.readline().strip().split(' '))
        A = [map(conv_hr, fd.readline().strip().split(' ')) for j in xrange(na)]
        B = [map(conv_hr, fd.readline().strip().split(' ')) for j in xrange(nb)]
        a, b = solve(A, B, t)
        fd2.write("Case #%i: %s %s\n" % (i + 1, a, b))
    fd.close()
    fd2.close()
