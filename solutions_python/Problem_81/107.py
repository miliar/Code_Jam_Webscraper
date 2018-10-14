'''
Created on 21-mei-2011

@author: tom
'''

def parse_input():
    file = open("rpi_large.txt", 'rU')
    entries = int(file.readline())
    results = []
    while entries > 0:
        entries -= 1
        result = []
        teams = int(file.readline())
        while teams > 0:
            teams -= 1
            wins = file.readline().strip()
            win_list = []
            for c in wins:
                if c == ".":
                    win_list.append(0)
                elif c == "0":
                    win_list.append(-1)
                elif c == "1":
                    win_list.append(1)
                else:
                    print "WTF?!"
            result.append(win_list)
        results.append(result)
    return results
        
# return: WP, OWP(this team won), OWP(this team lost)
def win_percentage(games):
    wins = 0
    total = 0
    for game in games:
        if game:
            total += 1
            if game == 1:
                wins += 1
    return 1.0*wins/total, 1.0*(wins-1)/(total-1), 1.0*wins/(total-1)

def calc_OWP(games, WP):
    result = 0
    total = 0
    for i, game in enumerate(games):
        if game:
            total += 1
            if game == 1:
                result += WP[i][2]
            elif game == -1:
                result += WP[i][1]
    return 1.0*result/total

def calc_OOWP(games, OWP):
    result = 0
    total = 0
    for i, game in enumerate(games):
        if game:
            total += 1
            result += OWP[i]
    return 1.0*result/total

def calculate_result(teams):
    WP = []
    for team in teams:
        WP.append(win_percentage(team))
    OWP = []
    for team in teams:
        OWP.append(calc_OWP(team, WP))
    OOWP = []
    for team in teams:
        OOWP.append(calc_OOWP(team, OWP))
    RPI = []
    for i, team in enumerate(teams):
        RPI.append(0.25*WP[i][0] + 0.5*OWP[i] + 0.25*OOWP[i])
    return RPI

def main():
    inputs = parse_input()
    results = []
    for input in inputs:
        results.append(calculate_result(input))
        
    output = open("output_rpi_large.txt", 'w')
    for i, result in enumerate(results):
        output.write("Case #%d:\n" % (i+1))
        for j, val in enumerate(result):
            output.write(str(val))
            if j < len(result)-1:
                output.write("\n")
        if i < len(results)-1:
                output.write("\n")
    output.close()

if __name__ == '__main__':
    main()