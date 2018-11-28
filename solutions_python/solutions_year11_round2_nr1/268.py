import sys

def new_matrix(n):
    return [[['.']for j in range(n)]for i in range(n)]

def echo(m):
    for team in m:
        print team




def wp(matrix, team, throwout= -1):
    wins = 0
    played = 0
    N = len(matrix)
    for opp in range(N):
        if matrix[team][opp] != '.' and opp != throwout:
            played += 1
            if matrix[team][opp] == '1': wins += 1
    return wins / (played * 1.0)



def owp(matrix, team):
    num_opp = 0
    sum_wp = 0
    N = len(matrix)
    for opp in range(N):
        if matrix[team][opp] != '.':
            num_opp += 1
            sum_wp += wp(matrix, opp, throwout=team)
    return sum_wp / (num_opp * 1.0)
    
def oowp(matrix, team):
    num_opp = 0
    sum_owp = 0
    N = len(matrix)
    for opp in range(N):
        if matrix[team][opp] != '.':
            num_opp += 1
            sum_owp += owp(matrix, opp)
    return sum_owp / (num_opp * 1.0)

def rpi(matrix, team):
    return 0.25 * wp(matrix, team) + 0.50 * owp(matrix, team) + 0.25 * oowp(matrix, team)

def solve(f):
    f = open(f)
    w = open('out.txt', 'w')
    # Read the number of cases
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        #N teams
        matrix = new_matrix(N)
        for i in range(N):
            matrix[i] = list(f.readline().rstrip())
        output = 'Case #%d:\n' % (t + 1)
        for team in range(N):
            output += str(rpi(matrix, team)) + '\n'
        print output
        w.write(output)
    
    f.close()
    w.close()




        
if __name__ == '__main__':
    solve('a-large.in')
#    print doit(10, 10, 100)
    
