"""
this solution uses scipy for array operations, available on scipy.org

usage: solution.py input.in > output.out
"""
import sys
import scipy

a = open(sys.argv[1])
# a = open('case.txt')

data = a.readlines()

a.close()

for case in range(long(data.pop(0))):
    teams = int(data.pop(0))
    results = scipy.zeros((teams,teams))
    for i in range(teams):
        line = data.pop(0)
        for j,char in enumerate(line):
            if char == '.':
                  results[i,j] = -1
            elif char == '1':
                  results[i,j] = 1

    WP = [[len(scipy.where(results[i,:]>0)[0]),
          len(scipy.where(results[i,:]>-1)[0])] for i in range(teams)]

    finalWP = scipy.zeros(teams)
    finalOWP = scipy.zeros(teams)
    for team in range(teams):
        finalWP[team] = float(WP[team][0])/WP[team][1]
        owp = []
        for oteam in scipy.where(results[team,:]>-1)[0]:
            if results[team,oteam]==1:
                owp.append( float(WP[oteam][0])/(WP[oteam][1]-1))
            elif results[team,oteam]==0:
                owp.append( float(WP[oteam][0]-1)/(WP[oteam][1]-1))
            else:
                owp.append(float(WP[oteam][0])/(WP[oteam][1]))
        owp = scipy.array(owp)
        finalOWP[team]=owp.mean()

    finalOOWP = scipy.zeros(teams)
    for team in range(teams):
        finalOOWP[team] = finalOWP[scipy.where(results[:,team]>-1)[0]].mean()

    #print finalWP, finalOWP, finalOOWP

    print "Case #"+str(case+1)+":"
    for team in range(teams):
         print 0.25*finalWP[team] + 0.5 * finalOWP[team] + 0.25*finalOOWP[team]

