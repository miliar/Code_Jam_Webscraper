import sys

if __name__ == '__main__':
    
    T = int(sys.stdin.readline())
    for case in xrange(T):
        N = int(sys.stdin.readline())
        candies = map(int, sys.stdin.readline().split())
        sum_candies = sum(candies)
        
        res = -1
        for i in xrange(1, 1 << N - 1):
            xor1, xor2 = 0, 0
            for j, c in enumerate(candies):
                if i & (1 << j):
                    xor1 ^= c
                else:
                    xor2 ^= c
            
            if xor1 == xor2:
                summ = sum(c for j, c in enumerate(candies) if i & (1 << j))
                res = max(res, summ, sum_candies - summ)
        
        if res == -1:
            res = 'NO'
        
        sys.stdout.write("Case #%s: %s\n" % (case + 1, res))