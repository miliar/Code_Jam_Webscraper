import sys

C = input()

for i in xrange(C):
    N = input()
    M = input()
    customers = {}
    for j in xrange(M):
        split = sys.stdin.readline().rstrip().split(' ')
        T = int(split[0])
        split = split[1:]
        liked = set()
        for k in xrange(T):
            raw_flavor, malted = split[:2]
            liked.add((int(raw_flavor) - 1, int(malted)))
            split = split[2:]
        customers[j] = liked
        
    def compute(flavors):
        if len(flavors) == N:
            for liked in customers.values():
                for item in enumerate(flavors):
                    if item in liked:
                        break
                else:
                    return None
            else:
                return flavors
                
        a1 = compute([0] + flavors)
        if a1:
            return a1
        return compute([1] + flavors)
    
    answer = compute([])
    if not answer:
        print 'Case #%d: IMPOSSIBLE' % (i + 1)
    else:
        print 'Case #%d: %s' % (i + 1, ' '.join(str(malted) for malted in answer))
