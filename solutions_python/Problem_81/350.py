def avg(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return 1.0 * sum / len(a)

def appendWP(v, number):
    # every team
    for q in range(number):
        # calculate wp
        games = []
        for r in range(number):
            if v[q][r] != '.': games.append(int(v[q][r]))
        v[q].append(avg(games))
    return v

def calculateWPwithoutTeam(v, team, ex, count):
    l = []
    for g in range(count):
        if (g != ex) and (v[team][g] != '.'):
            l.append(int(v[team][g]))
    return avg(l)

def calculateOWP(v, team, count):
    l = []
    for game in range(count):
        if v[team][game] != '.':
            l.append(calculateWPwithoutTeam(v, game, team, count))
    return avg(l)

def appendOWP(v, count):
    # every team
    for team in range(count):
        # calculate owp
        v[team].append(calculateOWP(v, team, count))
    return v

def calculateOOWPfrom(v, player, count):
    values = []
    for p in player: values.append(v[p][count+1])
    return avg(values)

def appendOOWP(v, count):
    for t in range(count):
        played_against = []
        for g in range(count):
            if v[t][g] != '.': played_against.append(g)
        v[t].append(calculateOOWPfrom(v, played_against, count))
    return v

def calculate(v, number):
    v = appendWP(v, number)
    v = appendOWP(v, number)
    v = appendOOWP(v, number)

    n = number

    result = []
    for i in range(number):
        result.append(round(0.25*v[i][n] + 0.5*v[i][n+1] + 0.25*v[i][n+2],12))

    results = ''
    for i in result:
        results += str(i) + '\n'

    return results

# i-o
fIn     = open('aInput', 'r')
fOut    = open('aOutput', 'r+')


fIn = fIn.readlines()
fIn = fIn[1:]

j = 1

while fIn:
    count = int(fIn[0])
    fIn = fIn[1:]

    values = []
    for i in range(count):
        r = []
        for q in fIn[0][:-1]:
            r.append(q)
        values.append(r)
        fIn = fIn[1:]

    fOut.write("Case #" + str(j) + ": \n" + calculate(values, count))
    j += 1
