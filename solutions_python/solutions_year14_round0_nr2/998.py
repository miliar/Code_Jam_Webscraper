import sys
def solve(C,F,X):
    sum = 0.0
    current_rate = 2.0
    while True:
        a = X/current_rate
        b = C/current_rate + X/(current_rate+F)

        if a <= b:
            sum += a
            break
        sum += C/current_rate    
        current_rate += F
        #print a,b,sum,current_rate
    return sum


T = int(sys.stdin.readline().strip())
case = 1
for _ in xrange(T):
    C,F,X = map(float,sys.stdin.readline().strip().split())
    print "Case #%d: %.7f" %(case, solve(C,F,X))
    case += 1
