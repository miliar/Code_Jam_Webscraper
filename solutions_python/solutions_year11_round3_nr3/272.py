import sys

def read_case(infile):
    N, L, H = map(int, infile.readline().strip().split())
    freq = map(int, infile.readline().strip().split())
    assert len(freq) == N
    return (L, H, freq)

def solve_case(L, H, freq):
    jeff = []
    for j in range(L, H + 1):
        good = True
        for f in freq:
            if j % f != 0 and f % j != 0:
                good = False
                break
        if good:
            jeff.append(j)
    if len(jeff) == 0:
        return "NO"
    else:
        jeff.sort()
        return str(jeff[0])
if __name__ == '__main__':
    infile = sys.stdin
    T = int(infile.readline())      
    for i in range(T):
        (L, H, freq) = read_case(infile)
        result = solve_case(L, H, freq)
        print "Case #%d: %s" % (i + 1, result)
    
