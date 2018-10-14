import fileinput
from multiprocessing import Pool

import psyco
psyco.full()

def simulateStep(old_grid,new_grid):
    got_one = False
    for x in range(len(old_grid)):
        for y in range(len(old_grid[x])):
            if old_grid[x-1][y] == True and old_grid[x][y-1] == True:
                new_grid[x][y] = True
                got_one = True
            elif old_grid[x][y] == True and (old_grid[x-1][y] == True or old_grid[x][y-1] == True):
                new_grid[x][y] = True
                got_one = True
            else:
                new_grid[x][y] = False
    return got_one


def solve(problem):
    grid_a = problem
    grid_b = []
    got_one = False
    for x in range(len(problem)):
        grid_b.append([False]*len(problem[x]))
        if max(problem[x]):
            got_one = True
    if not got_one:
        return 0
    step_count = 1
    while simulateStep(grid_a,grid_b):
##        for l in grid_a:
##            print l
##        print "---"
##        for l in grid_b:
##            print l
##        print "==="
        grid_c = grid_a
        grid_a = grid_b
        grid_b = grid_c
        step_count += 1
    return step_count

def parseProblems(it,caseCount):
    problems = []
    for x in range(caseCount):
        c = int(it.next())
        lines = []
        max_x = 0
        max_y = 0
        for i in range(c):
            [x1,y1,x2,y2] = map(int, it.next().split())
            lines.append([x1,y1,x2,y2])
            max_x = max([x1,x2,max_x])
            max_y = max([y1,y2,max_y])
        problem = []
        for x in range(max_x+2):
            problem.append([False]*(max_y+2))
##        print lines
        for l in lines:
            for x in range(l[0]+1,l[2]+2):
                for y in range(l[1]+1,l[3]+2):
##                    print "Setting",x,y
                    problem[x][y] = True
        problems.append(problem)        
    return problems

def main():
    it = fileinput.input()
    caseCount = int(it.next())
    pool = Pool(processes=2)              # start 4 worker processes

    problems = parseProblems(it,caseCount)
    #solutions = pool.map(solve, problems)
    solutions = map(solve, problems)

    for x in enumerate(solutions):
        print "Case #%d: %s" % (x[0]+1,x[1])

if __name__ == "__main__":
    main()
