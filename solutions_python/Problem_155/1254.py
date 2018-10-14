import sys

readline = sys.stdin.readline

num_cases = int(readline())


for icase in xrange(1, num_cases + 1):
    line = readline()

    tot_ppl = 0
    num_invite = 0


    start = 0
    for start, c in enumerate(line.strip()):
        if c == ' ':
            start += 1
            break

    for num_required, c in enumerate(line[start:].strip()):
        num_at_pos = int(c)
        if tot_ppl < num_required:
            n = num_required - tot_ppl
            num_invite += n
            tot_ppl += n
        tot_ppl += num_at_pos

    print 'Case #%s: %s' % (icase, num_invite)
