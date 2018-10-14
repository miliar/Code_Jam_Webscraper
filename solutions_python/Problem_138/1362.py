inp = open('d-in', 'r')
out = open('d-out', 'w')
# import sys
# out = sys.stdout

cases = int(inp.next())
print cases
for case in xrange(cases):
    inp.next()
    nb = map(float, inp.next().strip().split())
    kb = map(float, inp.next().strip().split())
    nb.sort()
    kb.sort()

    # print [x for x in nb if x > kb[0]]
    count_deceit = 0
    ni = 0
    for i, k in enumerate(kb):
        while ni < len(nb) and nb[ni] < k:
            ni += 1
        if ni < len(nb):
            # print nb[ni], k
            count_deceit += 1
            ni += 1
        else:
            break

    count = 0
    ki = 0
    for i, n in enumerate(nb):
        while ki < len(kb) and kb[ki] < n:
            ki += 1
        if ki < len(kb):
            # print kb[ki], n
            count += 1
            ki += 1
        else:
            break

    out.write('Case #{}: {} {}\n'.format(case + 1, count_deceit, len(nb) - count))
