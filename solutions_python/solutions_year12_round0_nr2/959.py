'''
Solution to Problem 2 in GCI 2012's Qualifiction Round.

(C) 2012 Aviral Dasgupta.
www.aviraldg.com
'''

from math import floor, ceil

# x  |x  |x 3x = T
# x  |x  |x-1 3x -1 = T
# x  |x-1|x-1 3x -2 = T

# x  |x  |x-2 }/ 3x - 2 = T # not applicable as #3 is a better fit
# x  |x-2|x-1 }\ Surprising 3x -3 = T
# x  |x-2|x-2 }/ Triplets 3x -4 = T

def get_solution(points, s, p):
    maxno = 0
    for point in points:
        if any((point/3 >= p, (point+1)/3 >= p, (point+2)/3 >= p)):
            maxno += 1
            continue
        elif s > 0:
            if point < p:
                continue
            if any(((point+3)/3 >= p, (point+4)/3 >= p)):
                s -= 1
                maxno += 1
    return maxno

def main():
    N = int(raw_input())
    for i in xrange(N):
        # discard n, not needed
        inp = map(int, raw_input().split(' ')[1:])
        s = inp.pop(0)
        p = inp.pop(0)
        print 'Case #{0}: {1}'.format(i+1, get_solution(inp, s, p))

if __name__=='__main__':
    main()
