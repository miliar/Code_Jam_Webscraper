import sys

inf = open(sys.argv[1])

t = int(inf.readline())

# N S p
# N = number of Googlers
# S = number of surprising triplets
# p = score p
# t_i = total points of Googlers

for li in range(0, t):
    line = inf.readline().strip()
    parts = line.split()
    n = int(parts.pop(0))
    s = int(parts.pop(0))
    p = int(parts.pop(0))
    scores = parts

    certain = 0
    possible = 0
    for score in scores:
        score = int(score)
        flr = score / 3
        rem = score % 3

        if score == 0 and p > 0:
            continue

        if flr >= p:
            certain += 1
        elif flr == p-1 and rem > 0:
            certain += 1
        elif flr == p-1 and rem == 0:
            possible += 1
        elif flr == p-2 and rem == 2:
            possible += 1

    print "Case #%i: %i" % (li+1, certain + min(possible,s))
