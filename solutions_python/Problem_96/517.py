import sys

f = sys.stdin
T = int(f.readline())

for j in range(T):
    l = map(lambda x: int(x), f.readline().split() )
    N,S, p, l = l[0], l[1], l[2], l[3:]
    l.sort(reverse=True)
    high = 0
    for val in l :
        r = val % 3
        i = val/3
        if r == 2:
            if i+1 >= p : ## i, i+1, i+1
                high += 1
            elif S > 0 and i+2 >= p : ## i, i, i+2
                high += 1
                S -= 1
        elif r == 0:
            if i >= p : ## i, i, i
                high += 1
            elif S > 0 and i+1 >= p and i-1 >= 0: ## i-1, i, i+1
                high += 1
                S -= 1
        elif r == 1:
            if i+1 >= p :
                high += 1
    print 'Case #{}:'.format(j+1),high
