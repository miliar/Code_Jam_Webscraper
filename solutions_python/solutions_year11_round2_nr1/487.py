'''
Created on May 22, 2011

@author: doronv
'''

# import section
import sys

# set example flag
if (len(sys.argv) > 3) and (sys.argv[3] == '-e'): 
    example = True
else:
    example = False 

# open input and output
input = open(sys.argv[1],'r')
output = open(sys.argv[2],'w')

# read case number
T = int(input.readline())

# iterate on all cases
for t in range(T):

    # read number of teams
    N = int(input.readline())
    
    games = [[0 for i in range(N)] for j in range(N)]
    
    # read each team's line and build a matrix with all results
    for n in range(N):
        for i in range(N):
            ch = input.read(1)
            if (ch == '0'):
                games[n][i] = -1
            if (ch == '.'):
                games[n][i] = 0
            if (ch == '1'):
                games[n][i] = 1
        input.readline()

    # reset arrays
    WP = [0.0 for i in range(N)];
    total = [0.0 for i in range(N)];
    OWP = [0.0 for i in range(N)];
    OOWP = [0.0 for i in range(N)];

#    if (t == 1):
#        games = [[0,1, 1, 0], [-1, 0, -1, -1], [-1, 1, 0, 1], [0, 1, -1, 0]]
    
#    print games
    
    # calculate all WPs and total games first
    for n in range(N):
        for i in range(N):
            # count wins
            if (games[n][i] == 1):
                WP[n] = WP[n] + 1
            # count total games
            if (games[n][i] != 0):
                total[n] = total[n] + 1
        # divide by total opponents
        WP[n] = WP[n] / total[n]
            
    # calculate OWPs now
    for n in range(N):
        for i in range(N):
            # don't count none opponents
            if (games[n][i] != 0):
                # recalculate the other team's WP without the game against team n
                if (games[n][i] == 1):
                    # don't touch the wins number
                    OWP[n] = OWP[n] + ((WP[i] * total[i]) / (total[i] - 1))
                if (games[n][i] == -1):
                    # remove one win
                    OWP[n] = OWP[n] + ((WP[i] * total[i] - 1) / (total[i] - 1))
                    
        # divide by number of opponents
        OWP[n] = OWP[n] / total[n]
    
    # calculate all OOWPs now
    for n in range(N):
        for i in range(N):
            # don't count none opponents
            if (games[n][i] != 0):
                OOWP[n] = OOWP[n] + OWP[i]
        # divide by number of opponents
        OOWP[n] = OOWP[n] / total[n]
    
    # output case result
    outputLine = 'Case #' + str(t + 1) + ':\n'
    if (example):
        print(outputLine)
    output.write(outputLine)
    for n in range(N):
        # do RPI and output 
        outputLine = '%.12f'%(0.25 * WP[n] + 0.5 * OWP[n] + 0.25 * OOWP[n]) + '\n'
        if (example):
            print(outputLine)
        output.write(outputLine)

# close input and output 
input.close()
output.close()

# if this is an example run then compare the output to the example output file
if (example):
    output = open(sys.argv[2])
    example = open(sys.argv[4])
    
    equal = True;
    
    while(1):
        outputC = output.read(1)
        exampleC = example.read(1)
        if (outputC!=exampleC):
            equal = False
            break
        if (not outputC):
            break;

    if (equal):
        print('example results match OK')
        sys.exit(0)
    else:
        print('ERROR: example result differs from given output')
        sys.exit(1)