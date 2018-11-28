def flip(cakes,k):
    cakes = list(cakes)
    count = 0
    for i in range(len(cakes)):
        if cakes[i] == '-':
            if (i + k) > len(cakes):
                return 'IMPOSSIBLE'
            else:
                cakes[i:i+k] = ['-' if c == '+' else '+' for c in cakes[i:i+k]]
                count += 1
    return count

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    cakes, k = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, flip(cakes, int(k)))


