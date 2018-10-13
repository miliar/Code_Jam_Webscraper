# Code Jam 2012 - Qualifying Round
# Problem C - Recycled Numbers

#import itertools

### we know that we can terminate after we meet another ????

income = open('C-small-attempt0.in','rU')
outcome = open('C-small-attempt0.out','w')

def combos(integer, limit): # expect both in int form
    foo = list(str(integer) + str(integer))
    possible = [] # generate a list of crap
    okay = []
    for x in range(len(str(integer))):
        possible.append(''.join(foo[x:x+len(str(integer))]))
    for x in possible:
        if x[0] == '0':
            continue
        if int(x) <= limit and int(x) > integer and int(x) not in okay:
            okay.append(int(x))
    return okay # list of int
cat = [] #debug
lineState = 0
#lowest = 100000000 # keep track of the lowest m, check this is outside the range
#Step 1, iterate over n, starting with A
for line in income:
    if lineState == 0: # first line
        #line = line.rstrip
        cases = int(''.join(line.rstrip().split(' ')))
        lineState += 1
        continue
    
    count = 0 # the running total of recycled pairs for a given A,B
    
    line = line.rstrip() # kill that \n
    cat.append(line.split(' ')) #debug
    line = line.split(' ') # now it's a list of str
    A = int(line[0])
    B = int(line[1]) # upper and lower limits for m,n
    
    for n in range(A,B): # lowest should end up smaller than m
        stuff = sorted(combos(n,B))
        if len(stuff) == 0: # cases where recycling is impossible e.g. 4 => []
            continue
##        if stuff[0] < lowest: # optimisation, check later
##            lowest = stuff[0]
        count += len(stuff)

    #print("Case #%d: %d" % (lineState, count))
    outcome.write('Case #%d: %d' % (lineState, count))
    if lineState != cases:
        outcome.write('\n')
    lineState += 1
        
#Step 2, generate all cyclic m, see def combos
#Step 3, check all m: if m > n AND m <= B, add to count
## optimise: keep track of lowest m
#Step 4, next n
#Step 5, output in desired format (debug with print first)

income.close()
outcome.close()
