from math import *

# Solve only the small dataset
def solve(Ac, Aj, Actasks, Ajtasks):
    Actasks.sort()
    Ajtasks.sort()

    tasks = [[i,0] for i in Actasks] + [[j,1] for j in Ajtasks]
    tasks.sort()

    ctime = sum([i[1]-i[0] for i in Actasks])
    jtime = sum([i[1]-i[0] for i in Ajtasks])

    freectime = 720 - ctime
    freejtime = 720 - jtime


    print(ctime, freectime,jtime, freejtime)

    print(tasks)

    if len(tasks) == 1:
        if tasks[0][0][0] >= 720:
            return 2
        elif tasks[0][0][1]<=720:
            return 2
        else:
            return 2
    elif len(tasks) == 2:
        if tasks[0][1] == tasks[1][1]:
            if tasks[1][0][1]-tasks[0][0][0] <= 720:
                return 2
            elif tasks[1][0][0] - tasks[0][0][1] == 720:
                return 2
            elif tasks[0][0][1] + (1440-tasks[1][0][0]) <= 720:
                return 2
            else:
                return 4
                
            #return 50
        else:
            if tasks[0][0][1] <= 720:
                return 2
            elif tasks[1][0][0] >= 720:
                return 2
            else:
                return 4
    else:
        return 0

    return 0

f = open('B-small-attempt0.in','r')
g = open('output.txt','w')

T = int(f.readline())
for ind in range(T):
    # read input
    [Ac,Aj] = [int(i) for i in f.readline().split()]
    Actasks = [[int(i) for i in f.readline().split()] for j in range(Ac)]
    Ajtasks = [[int(i) for i in f.readline().split()] for j in range(Aj)]

    # compute answer
    ans = solve(Ac, Aj, Actasks, Ajtasks)

    # print to file
    g.write('Case #{}: {}\n'.format(ind+1,ans))

f.close()
g.close()

