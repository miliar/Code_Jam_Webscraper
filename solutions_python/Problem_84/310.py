'''
Created on May 23, 2011

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

print T,
# iterate on all cases
for t in range(T):
    # get R and C
    values = input.readline().split(' ')
    R = int(values[0])
    C = int(values[1])

    picture = [['' for r in range(C)] for c in range(R)]
    
    # get P and V
    for r in xrange(R):
        for c in range(C):
            ch = input.read(1)
            picture[r][c] = ch
        input.readline()
            
    # start tiling            
    Done = False
    Failed = False
    while (not Done):
        for r in xrange(R):
            for c in range(C):
                # this has to be upper left corner
                if (picture[r][c] == '#'):
                    # check that we have room
                    if (r < R - 1) and (c < C - 1):
                        # check that we can tile
                        if ((picture[r][c + 1] == '#') and 
                            (picture[r + 1][c] == '#') and 
                            (picture[r + 1][c + 1] == '#')):
                            # tile
                            picture[r][c] = '/'
                            picture[r][c + 1] = '\\' 
                            picture[r + 1][c] = '\\' 
                            picture[r + 1][c + 1] = '/'
                        else:
                            Failed = True
                    else:
                        Failed = True
                    
                if Failed:
                    continue
            if Failed:
                continue
        Done = True

    # output case result
    
    outputLine = 'Case #' + str(t + 1) + ':\n'
    if (example):
        print outputLine, 
    output.write(outputLine)

    if Failed:
        outputLine = "Impossible\n"
        if (example):
            print outputLine,
        output.write(outputLine)
    
    else:
        for r in xrange(R):
            outputLine = ''
            for c in range(C):
                outputLine = outputLine + picture[r][c]
            outputLine = outputLine + '\n' 
            if (example):
                print outputLine,
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