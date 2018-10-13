import sys

def read_input(f):
    A, B, K = ( int(field) for field in f.readline().strip().split() )
    return A, B, K

def count_possible_pairs(A, B, K):
    if A < B:
        A, B = B, A
    count = 0
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                count += 1
    return count

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in xrange(1, T + 1):
        A, B, K = read_input(f)
        print "Case #%d:" %case,
        print count_possible_pairs(A, B, K)
