import sys

fname = sys.argv[1]
f = open(fname)

tline = f.readline().strip()
t = int(tline)

def optimal(armin, motes):
    if not motes:
        return 0
    else:
        if motes[0] < armin:
#            print "ok"
            return optimal(armin + motes[0], motes[1:])
        elif armin < 2:
            return 1 + optimal(armin, motes[1:])
        else:
#            print "branch"
            return 1 + min(optimal(armin + armin - 1, motes),
                           optimal(armin, motes[:-1]))

def eat(armin, motes):
    while motes and armin > motes[0]:
        armin += motes[0]
        motes = motes[1:]
    return armin, motes

for i in range(t):
    abline = f.readline().strip()
    moteline = f.readline().strip()
    a, b = (int(x) for x in abline.split())
    motes = [int(x) for x in moteline.split()]
    motes.sort()
    largest = motes[-1]

#    print a, b, motes
    changes = optimal(a, motes)
#     while False and motes:
#         a, motes = eat(a, motes)
#         if motes:
#             if a == 1:
#                 motes = motes[:-1]
#             else:
#                 motes = [a-1] + motes
#             changes += 1
    print "Case #%i: %i" % (i + 1, changes)
