from sys import stdin

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    data = stdin.readline().split()
    C = int(data[0])
    combs = {x[k]+x[1-k]:x[2] for x in data[1:C+1] for k in xrange(2)}
    D = int(data[C+1])
    opps = {}
    for datum in data[C+2:C+D+2]:
        d1 = datum[0]
        d2 = datum[1]
        if not opps.has_key(d1):
            opps[d1] = {}
        if not opps.has_key(d2):
            opps[d2] = {}
        opps[d1][d2] = 1
        opps[d2][d1] = 1
    invocation = data[-1]
    spell = []
    for base in invocation:
        spell += [base]
        if len(spell) >= 2:
            if combs.has_key(spell[-2]+spell[-1]):
                spell = spell[:-2] + [combs[spell[-2]+spell[-1]]]
        if len(spell) >= 2:
            if opps.has_key(spell[-1]):
                if len([z for z in spell if opps[spell[-1]].has_key(z)]) > 0:
                    spell = []
    print "Case #" + str(case_index) + ": " + str(spell).replace("'","")
