def get_scores(surprising, nb, scores):
    n = 0
    for i in scores:
        best = i/3 + (1 if i%3 else 0)
        if best >= nb:
            n += 1
        elif surprising > 0 and best > 0 and best == nb-1 and (i%3 == 0 or i%3 == 2):
            n += 1
            surprising -= 1
    return n

nb_cases = int(raw_input())
for n in xrange(nb_cases):
    line = map(int,raw_input().split())
    print "Case #%s: %s"%(n+1, get_scores(line[1], line[2], line[3:]))
