import sys

num_cases = int(sys.stdin.readline().strip())

def flip(i, pancakes, k):
    for j in xrange(i, i + k):
        pancakes[j] = not pancakes[j]

for i in xrange(num_cases):
    pancakes, k = sys.stdin.readline().strip().split()
    k = int(k)
    pancakes = [(True if p == "+" else False) for p in pancakes]
    count = 0
    # print pancakes
    j = 0
    while j <= len(pancakes) - k:
        if not pancakes[j]:
            flip(j, pancakes, k)
            count += 1
        j += 1
    filtered = [p for p in pancakes if not p]
    if len(filtered):
        print "Case #%d: IMPOSSIBLE" % (i + 1)
    else:
        print "Case #%d: %d" % (i + 1, count)
