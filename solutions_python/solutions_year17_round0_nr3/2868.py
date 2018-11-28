import math


def solve(spans, k):
    #print spans, k
    largest_span = max(spans)

    if k <= spans[largest_span]:
        return [int(math.ceil((largest_span - 1)/2.)), int(math.floor((largest_span - 1)/2.))]

    adding = spans.pop(largest_span)
    spans[int(math.ceil((largest_span - 1) / 2.))] = adding + spans.get(int(math.ceil((largest_span - 1) / 2.)), 0)
    spans[int(math.floor((largest_span - 1) / 2.))] = adding + spans.get(int(math.floor((largest_span - 1) / 2.)), 0)

    return solve(spans, k - adding)

cases = int(raw_input())
for case in xrange(cases):
    [N, K] = map(int, raw_input().split())
    print "Case #%d: " % (case + 1), ' '.join(str(p) for p in solve({N: 1}, K))
