import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    (A, B) = [int(x) for x in f.readline().split()]

    total = 0
    for n in range(A, B):
        candidates = []
        temp = str(n)
        for pivot in range(1, len(temp)):
            candidates.append(temp[pivot:] + temp[:pivot])
        candidates = [int(x) for x in candidates]
        seen = set()
        for candidate in candidates:
            if candidate > n and candidate <= B:
                if candidate not in seen:
                    total += 1
                    seen.add(candidate)

    print "Case #%d: %d" % (case + 1, total)
