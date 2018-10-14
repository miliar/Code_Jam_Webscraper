#! /usr/bin/python
#RPI

import sys, os

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

pos = 1
for c in range(cases):
    N = int(lines[pos].strip())
    data = [lines[pos+1+i].strip() for i in range(N)]
    inputData.append( data )
    pos = pos + 1 + N


def analyse(data):
    print(data)
    teams = len(data[0])
    games_won = [0 for j in range(teams)]
    games_played = [0 for j in range(teams)]
    for i in range(teams):
        for j in range(i,teams):
            if data[i][j] <> '.':
                games_played[i] =  games_played[i] + 1
                games_played[j] =  games_played[j] + 1
                if data[i][j] == '1':
                    games_won[i] = games_won[i] + 1
                else:
                    games_won[j] = games_won[j] + 1
    print('games_played',games_played)
    print('games_won',games_won)
    WP = [ 1.0*gw/gp for gp,gw in zip(games_played, games_won) ]
    print('WP',WP)
    OWP = []
    for i in range(teams):
        n_games_won = games_won[:]
        n_games_played = games_played[:]
        for j in range(teams):
            if data[i][j] <> '.':
                #n_games_played[i] = n_games_played[i] - 1
                n_games_played[j] = n_games_played[j] - 1
                if data[i][j] == '1':
                    n_games_won[i] = n_games_won[i] - 1
                else:
                    n_games_won[j] = n_games_won[j] - 1
            else:
                n_games_won[j] = 0
        n_games_won[i] = 0
        #print('  n_games_played',n_games_played)
        #print('  n_games_won',n_games_won)
        n_WP = [ 1.0*gw/gp for gp,gw in zip(n_games_played, n_games_won) ]
        OWP.append(sum( n_WP ) / games_played[i])
    print('OWP', OWP)
    def average(alist):
        return 1.0*sum(alist)/len(alist)
    OOWP = []
    for i in range(teams):
        OOWP.append(average( [ owp for j,owp in enumerate(OWP) if  data[i][j] <> '.'] ) )
    print('OOWP', OOWP)
    RPI = [0.25 * wp + 0.50 * owp + 0.25 * oowp for wp, owp, oowp in zip(WP,OWP,OOWP)]
    return '\n' + '\n'.join(['%15.13f' % rpi for rpi in RPI])

output = []
for case,input in enumerate(inputData):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
