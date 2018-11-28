import pprint

f = open('A-small-attempt0.in', 'r')
numCases = int(f.readline())
numCasesCpy = numCases+1
tricks = [None]*numCases

while numCases > 0:
    answer1 = int(f.readline())-1
    grid1 = [None]*4
    line1 = f.readline().split()
    grid1[0] = line1
    line2 = f.readline().split()
    grid1[1] = line2
    line3 = f.readline().split()
    grid1[2] = line3
    line4 = f.readline().split()
    grid1[3] = line4
    answer2 = int(f.readline())-1
    grid2 = [None]*4
    line1 = f.readline().split()
    grid2[0] = line1
    line2 = f.readline().split()
    grid2[1] = line2
    line3 = f.readline().split()
    grid2[2] = line3
    line4 = f.readline().split()
    grid2[3] = line4
    yourCards = set(grid1[answer1]).intersection( set(grid2[answer2]) )
    if len(yourCards) > 1:
        print "Case #"+str(numCasesCpy-numCases)+": Bad magician!"
    elif len(yourCards) == 0:
        print "Case #"+str(numCasesCpy-numCases)+": Volunteer cheated!"
    else:
        print "Case #"+str(numCasesCpy-numCases)+": "+str(yourCards.pop())
    numCases = numCases-1
