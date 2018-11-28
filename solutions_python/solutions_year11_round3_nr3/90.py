import sys

def solve(input):
    T = int(input.readline())
    for t in xrange(1, T+1):
        N, L, H = [int(x) for x in input.readline().split()]
        players = [int(x) for x in input.readline().split()]
        result = 0
        for freq in xrange(L, H+1):
            for p in players:
                if freq % p != 0 and p % freq != 0:
                    break
            else:
                result = freq
                break
        if result:
            print "Case #%d:" % t, result
        else:
            print "Case #%d:" % t, "NO"

if __name__ == '__main__':
    solve(sys.stdin)