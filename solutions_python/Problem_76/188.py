import sys

def solve_test(test):
    candies = map(int, test)
    if reduce(lambda x,y: x^y, candies) != 0:
        return 'NO'
    else:
        return str(sum(candies)-min(candies))

sequence = sys.stdin.readlines()
    
numtests = int(sequence[0])
for i in range(numtests):
    print 'Case #%d: %s' % (i+1,solve_test(sequence[2*i+2].split()))
