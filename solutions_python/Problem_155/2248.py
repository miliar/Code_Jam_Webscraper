

with open("A-large.in", 'r') as rp:
    lines = rp.read().strip().split('\n')
    num_cases = int(lines[0])
    for case_no, case in enumerate(lines[1:]):
        total, counts = case.split()
        num_total = int(total)
        counts = map(int, list(counts))
        partial_sums = [0] * (num_total + 1)
        for i in xrange(num_total + 1):
            partial_sums[i] = sum(counts[:i+1])
        loss = [max(0, i - partial_sums[i-1]) for i in xrange(1, num_total + 1)]
        print "Case #{0}: {1}".format(case_no + 1, max(loss) if loss else 0)
