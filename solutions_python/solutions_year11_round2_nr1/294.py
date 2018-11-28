def average(values):
    return sum(values, 0.0) / len(values)

def wp(results):
    return average([{"lose":0, "win":1}[x] for (_, x) in results])

casenum = 1
def doit(case):
    global casenum

    gameresults = {}
    opponents = {}

    for team, gameset in enumerate(case):
        gameresults[team] = [(opteam, ["lose","win"][int(game)]) for opteam, game in enumerate(gameset) if game != '.']
        opponents[team] = [opteam for (opteam, _) in gameresults[team]]

    WP = {}
    OWP = {}
    for team, results in gameresults.items():
        WP[team] = wp(results)
        OWP[team] = average([wp([x for x in gameresults[opteam] if x[0] != team]) for opteam in opponents[team]])

    OOWP = {}
    for team in gameresults.keys():
        OOWP[team] = average([OWP[opteam] for opteam in opponents[team]])

    print 'Case #%d:' % casenum
    for i in range(len(opponents.keys())):
        print 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
    casenum += 1

raw = [x.strip() for x in open('A-large.in').readlines()]
ZZZ = int(raw[0])

pos = 0
data = raw[1:]
for case in range(ZZZ):
    size = int(data[pos])
    pos += 1

    casedata = []
    for i in range(size):
        casedata.append(data[pos])
        pos += 1

    doit(casedata)
