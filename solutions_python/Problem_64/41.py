from sys import argv
from itertools import * 


f = open(argv[1])
def readline(): return f.readline()
def readint(): return int(f.readline())
def readarray(): return [int(x) for x in f.readline().split()]

def parse_char_bits(c):
    x = '0123456789ABCDEF'.index(c)
    a = []
    for i in xrange(4):
        x, r = divmod(x, 2)
        a.append(r)
    return [c for c in reversed(a)]
    
def parse_bits(line):
    return chain(*[parse_char_bits(c) for c in line.strip()])

def parse_board_line():
    return [b for b in parse_bits(readline())]

def parse_board(M):
    return [parse_board_line() for m in xrange(M)]


def zboard(M, N):
    return [[0 for n in xrange(N)] for m in xrange(M)]

def calc(A, M, N):
    m_x = zboard(M, N)
    for m in xrange(M):
        if A[m][N-1] >= 0:
            m_x[m][N-1] = 1
        else:
            m_x[m][N-1] = 0
        for n in xrange(N-2, -1, -1):
            if A[m][n] != A[m][n+1] and A[m][n+1] >= 0:
                m_x[m][n] = m_x[m][n+1] + 1
            else:
                m_x[m][n] = 1

    m_y = zboard(M, N)
    for n in xrange(N):
        if A[M-1][n] >= 0:
            m_y[M-1][n] = 1
        else:
            m_y[M-1][n] = 0

        for m in xrange(M-2, -1, -1):
            if A[m][n] != A[m+1][n] and A[m+1][n] >= 0:
                m_y[m][n] = m_y[m+1][n] + 1
            else:
                m_y[m][n] = 1

    m_b = zboard(M, N)
    for m in xrange(M):
        if A[m][N-1] < 0:
            m_b[m][N-1] = 0
        else:
            m_b[m][N-1] = 1
    for n in xrange(N):
        if A[M-1][n] < 0:
            m_b[M-1][n] = 0
        else:
            m_b[M-1][n] = 1

    for m in xrange(M-2, -1, -1):
        for n in xrange(N-2, -1, -1):
            if A[m][n] < 0:
                m_b[m][n] = 0
            elif A[m][n] == A[m+1][n+1]:
                m_b[m][n] = min(m_b[m+1][n+1] + 1, m_x[m][n], m_y[m][n])
            else:
                m_b[m][n] = 1

    return m_x, m_y, m_b

def cut_max(A, M, N):
    m_x, m_y, m_b = calc(A, M, N)

    max_b, y, x = 0, 0, 0
    for m in xrange(M):
        for n in xrange(N):
            if m_b[m][n] > max_b:
                max_b, y, x = m_b[m][n], m, n

    for m in xrange(y, y+max_b):
        for n in xrange(x, x+max_b):
            A[m][n] = -1

    """
    print
    print "mx"
    for m in xrange(M):
        print m_x[m]

    print
    print "my"
    for m in xrange(M):
        print m_y[m]

    print
    print "mb"
    for m in xrange(M):
        print m_b[m]
    print max_b, y, x
    """

    return max_b

for t in xrange(readint()):
    M, N = readarray()
    A = parse_board(M)

    r = [0 for i in xrange(min(M, N))]

    """
    print
    print "brd"
    for m in xrange(M):
        print A[m]
    """

    while True:
        size = cut_max(A, M, N)
        if size == 0:
            break
        r[size-1] += 1

    print "Case #%d: %d" % (t+1, sum([1 for rr in r if rr > 0]))
    for i in xrange(len(r)-1, -1, -1):
        if r[i] > 0:
            print i+1, r[i]

