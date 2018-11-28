#! /usr/bin/python

def solve(total,games,games_won):
    rwp = []
    owp = []
    oowp = []
    answer = ''
    for team in range(0,n):
        rwp.append(0.0)
        if total[team]>0:
            rwp[team] = float(len(games_won[team]))/float(total[team])
    #print rwp
    for team1 in range(0,n):
        owp.append(0.0)
        for team2 in games[team1]:
            point = 1 if team1 in games_won[team2] else 0
            if total[team2]-1==0:
                wp = 0.0
            else:
                wp = float(len(games_won[team2])-point)/float(total[team2]-1)
            owp[team1] = owp[team1] + float(wp/len(games[team1]))
    #print owp
    for team1 in range(0,n):
        oowp.append(0.0)
        for team2 in games[team1]:
            oowp[team1] = oowp[team1] + owp[team2]/len(games[team1])
    #print oowp
    for team1 in range(0,n):
        rpi = 0.25 * rwp[team1] + 0.5 * owp[team1] + 0.25 * oowp[team1]
        answer = answer + '\n%.8f'%rpi
    return answer

if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        line = f.readline().split()
        n = int(line[0])
        total = []
        games = []
        games_won = []
        for i in range(0,n):
            total.append(0)
            games.append([])
            games_won.append([])
            line = f.readline()
            #print line
            for j in range(0,n):
                if line[j]!='.':
                    total[i] = total[i]+1
                    if line[j]=='1':
                        games_won[i].append(j)
                    games[i].append(j)
        #print total
        #print games
        #print games_won
        answer = solve(total,games,games_won)
        g.write("Case #%d:%s" % (case,answer))
        if case<cases:
            g.write("\n")

    f.close()
    g.close()