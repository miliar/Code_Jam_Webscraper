import operator
import sys



def solve(bag):
    bag.sort()

    if reduce(operator.xor, bag) != 0:
        return "NO"

    for i in range(1, len(bag)):
        if reduce(operator.xor, bag[i:]) == reduce(operator.xor, bag[:i]):
            return sum(bag[i:])



    


dataset = open(sys.argv[1])

T = int(dataset.readline())

for i in range(T):
    N = int(dataset.readline())
    C = [int(k) for k in dataset.readline().split()]
    print "Case #%d: %s" % (i + 1, solve(C))
        
