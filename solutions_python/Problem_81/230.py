# FUNCTIONS
def findwp(team, excluding):
    #if wp[team] != -1:
    #    return wp[team]
    played = 0
    won = 0
    for i in range(nteams):
        if table[team][i] == "." or i == excluding:
            continue
        played += 1
        if table[team][i] == "1":
            won += 1
    #wp[team] = float(won) / played
    return float(won) / played

def findowp(team):
    #if owp[team] != -1:
    #    return owp[team]
    opponents = 0
    totalwp = 0
    for i in range(nteams):
        if table[team][i] == ".":
            continue
        opponents += 1
        totalwp += findwp(i, team)
    #owp[team] = totalwp / opponents
    return totalwp / opponents

def findoowp(team):
    opponents = 0
    totalowp = 0
    for i in range(nteams):
        if table[team][i] == ".":
            continue
        opponents += 1
        totalowp += findowp(i)
    return totalowp / opponents

def findrpi(team):
    return 0.25 * findwp(team, -1) + 0.5 * findowp(team) + 0.25 * findoowp(team)

# PROGRAM
nteams = 0
table = [[".", "1", "1", "."], ["0", ".", "0", "0"], ["0", "1", ".", "1"], [".", "1", "0", "."]]
wp = []
owp = []

f = file("input.txt")
lines = f.readlines()
t = int(lines[0])
l = 0
for p in range(t):
    l += 1
    size = int(lines[l])
    table = []
    wp = [-1 for i in range(size)]
    owp = [-1 for i in range(size)]
    nteams = size
    for i in range(size):
        l += 1
        table += [[c for c in lines[l]]]
    print "Case #" + str(p + 1) + ":"
    for i in range(size):
        print findrpi(i)
