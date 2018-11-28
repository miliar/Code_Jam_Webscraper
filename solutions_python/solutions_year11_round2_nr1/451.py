def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def findGames(data):
    games = 0
    for i in data:
        if i != '.': games+=1
    return games

def findWP(data):
    wins = 0
    games = 0
    for i in data:
        if i == '1': wins+=1
        if i != '.': games+=1
    return float(wins)/games

def getWPWithoutTeam(WP, games, data, team):
    wins = WP * games
    if data[team] == '0': wins -= 1
    if data[team] != '.': games -= 1
    return wins / games

def solveCase(schedule):
    out = ""
    games = []
    for i in schedule:
        games.append(findGames(i))
    WP = []
    for i in schedule:
        WP.append(findWP(i))

    OWP = []
    for i in range(len(schedule)):
        avg = 0
        count = 0
        for j in range(len(schedule)):
            if j != i and schedule[i][j] != '.':
                avg += getWPWithoutTeam(WP[j], games[j], schedule[i], j)
                count += 1
        OWP.append(avg/count)

    OOWP = []
    for i in range(len(schedule)):
        avg = 0
        count = 0
        for j in range(len(schedule)):
            if j != i and schedule[i][j] != '.':
                avg += OWP[j]
                count += 1
        avg /= count
        OOWP.append(avg)

    for i in range(len(schedule)):
        out += '\n' + str(0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i])
    return out

def process(data):
    for i in range(len(data)): data[i] = explode(data[i], '\n')[0]
    out = ""
    i = 1
    for case in range(int(data[0])):
        if case > 0: out += '\n'
        out += "Case #" + str(case+1) + ": "
        n = int(data[i])
        schedule = []
        for j in range(int(n)): schedule.append(data[i+1+j])
        i += (1+int(n))
        out += solveCase(schedule)
    return out

def main(fn):
    iFile = open(fn + ".in", "r")
    oFile = open(fn + ".out", "w")
    print("Files opened.")

    data = []
    while True:
        line = iFile.readline()
        if not line: break
        data.append(line)

    out = process(data)
    print("Calculations complete. Outputting to file.")
    oFile.writelines(out)
    print("Output complete.")
    iFile.close()
    oFile.close()
    print("Files closed.")

main("large")
