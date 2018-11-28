f = open("C:/Users/Eric/dropbox/codejam/war-large.in")

lines = f.readlines()[1:]
tests = [lines[x:x+3] for x in xrange(0, len(lines), 3)]

num = 1

for test in tests:
    me = sorted([float(x) for x in test[1].split()])
    you = reversed(sorted([float(x) for x in test[2].split()]))
    score = 0
    for challenge in you:
        if me[-1] > challenge:
            me.pop()
            score += 1
    me = reversed(sorted([float(x) for x in test[1].split()]))
    you = sorted([float(x) for x in test[2].split()])
    score2 = 0
    for block in me:
        good = False
        for challenge in you:
            if challenge > block:
                you.remove(challenge)
                good = True
                break
        if not good:
            you.pop(0)
            score2 += 1
    print "Case #%s: %s %s" % (num, score, score2)
    num += 1
