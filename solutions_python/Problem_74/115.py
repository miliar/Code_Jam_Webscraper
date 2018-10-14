import sys
f = sys.stdin
rint = lambda: int(f.next())
def other(player):
    return {"O": "B", "B": "O"}[player]

t = rint()
for i in xrange(t):
    line = iter(f.next().split(" "))
    n = int(line.next())
    p = {"O": 1, "B": 1}
    turns = 0
    free = {"O": 0, "B": 0}
    for _ in xrange(n):
        player, position = line.next(), int(line.next())
        dist = abs(p[player] - position)
        this_turns = max(0, dist - free[player]) + 1
#        print p, free, player, position, this_turns
        turns += this_turns
        p[player] = position
        free[player] = 0
        free[other(player)] += this_turns
    print "Case #%d: %d" % (i + 1, turns)
