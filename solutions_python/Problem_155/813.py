import sys

if len(sys.argv) == 1:
    sys.stdin = open("A.in")
else:
    sys.stdin = open(sys.argv[1])
    sys.stdout = open(sys.argv[1].replace('.in', '') + '.out', 'w')

n_cases = input()

for case in xrange(1, n_cases + 1):
    _, counts = raw_input().split()

    shills = 0
    clapping = 0

    for shyness, count in enumerate(counts):
        if shyness > clapping:
            shills += shyness - clapping
            clapping = shyness
        clapping += int(count)

    print "Case #%d: %s" % (case, shills)
