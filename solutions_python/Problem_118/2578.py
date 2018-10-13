def sqrt(x):

    ans = 0
    while ans*ans < x:
        ans = ans + 1
    if ans*ans != x:
        return None
    else:
        return ans

def play(m, a, b):

    palindromes = [ x for x in m if x == x[::-1] ]
    root = [ str(sqrt(int(x))) for x in palindromes ]
    fair = set ([ x for x in root if x == x[::-1] ])
    return len(fair)

if __name__ == "__main__":

    f = open('Output.txt','w')
    f.seek(0)
    with open('C-small-attempt0.in') as sample:
        t = int(sample.readline())
        assert 1 <= t <= 100
        for case in range(t):
            elements = sample.readline().strip('\n').split()
            N = int(elements[0])
            M = int(elements[1])
            assert 1 <= N <= 1000
            assert 1 <= M <= 1000
            matrix = [ str(N + x) for x in xrange(M - N + 1)]
            l = play(matrix, N, M)
            f.write("Case #%d:"%(case+1) + " " + "%d\n"%l)
