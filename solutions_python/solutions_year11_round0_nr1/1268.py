#!/usr/bin/python 

def process(line):
    count = int(line[0])
    commands = list()
    lookup = list()
    individual_moves = dict()
    individual_moves['O'] = list()
    individual_moves['B'] = list()
    lcount = 1
    for n in range(count):
        commands.append(int(line[lcount+1]))
        if line[lcount] == 'O':
            individual_moves['O'].append(int(line[lcount+1]))
            lookup.append('O')
        elif line[lcount] == 'B':
            individual_moves['B'].append(int(line[lcount+1]))
            lookup.append('B')
        else:
            print "error: robot",line[lcount],"not found"
        lcount += 2
    return doit(commands,lookup,individual_moves)

def doit(commands,lookup,individual_moves):
    loc = dict()
    loc['O'] = 1
    loc['B'] = 1 
    if len(commands) <= 0: return 0;
    time = 0
    while len(commands) > 0:
        deltat = 0
        robot = lookup[0]
        if robot == 'O':
            otherrobot = 'B'
        else:
            otherrobot = 'O'
        goal = commands[0]
        deltat = 0
        if loc[robot] != goal:
            deltat += abs(goal - loc[robot])
            loc[robot] = goal
        #import pdb;
        #pdb.set_trace()
        # check move the other robot by as much as possible
        deltat += 1 # press the button
        if (len(individual_moves[otherrobot]) > 0):
            if (individual_moves[otherrobot][0] > loc[otherrobot]): # if robot needs to move forward 
                loc[otherrobot] += deltat
                if loc[otherrobot] > individual_moves[otherrobot][0]:
                    loc[otherrobot] = individual_moves[otherrobot][0]
            else:
                loc[otherrobot] -= deltat
                if loc[otherrobot] < individual_moves[otherrobot][0]:
                    loc[otherrobot] = individual_moves[otherrobot][0]
        time += deltat
        lookup.pop(0)
        commands.pop(0)
        individual_moves[robot].pop(0)
    return time

if __name__ == '__main__':
    infn = 'a'
    outfn = 'out.fn'
    out = open(outfn,'w')
    inf = open(infn,'r')
    input = inf.readlines()
    count = int(input[0])
    for n in range(count):
        print >> out, "Case #" + str(n+1) + ": " + str(process(input[n+1].rstrip().split()))


