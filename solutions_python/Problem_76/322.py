def solve(infile):
    input = open(infile)
    T = int(input.readline())
    for t in xrange(1, T+1):
        N = int(input.readline())
        C = [int(c) for c in input.readline().split()]
        C.sort()
        result = 0
        for n in xrange(1, N):
            if patrick_sum(C[:n]) == patrick_sum(C[n:]):
                sum1 = sum(C[:n])
                sum2 = sum(C[n:])
                result = max(result, sum1, sum2)
        if result:
            print "Case #%d:" % t, result
        else:
            print "Case #%d:" % t, "NO"
    input.close()
    
def patrick_sum(sequence):
    result = 0
    for seq in sequence:
        result ^= seq
    return result
    
if __name__ == '__main__':
    import sys
    solve(sys.argv[1])
