# import string
# import math

income = open("A-small-attempt0-password.in","rU")
outcome = open("A-small-attempt0-password.out","w")

def prod(thelist, iterate): # do not feed zero
    """list of numbers, int"""
    out = 1
    for x in range(0,iterate):
        out *= thelist[x]
    return out

#lineCount = 0
lineState = 0 # check for first line
caseCount = 0
for line in income:
    if lineState == 0:
        total = int(line)
        lineState += 1
        caseCount += 1
        #lineCount += 1
        continue
    #do real stuff here
    elif lineState == 1: # getting A and B
        #cats = line #bug
        #print(line) # bug
        line = line.rstrip() # destroy newline
        line = line.split(' ') # list of string
        A = int(line[0])
        B = int(line[1]) # establish the inputs
        lineState += 1
        #lineCount += 1
        continue
    elif lineState == 2: # real stuff here
        line = line.rstrip()
        line = line.split(' ')
        prob = [] # list of probabilities
        for a in line: # refers to the list
            if '.' not in a:
                prob.append(int(a))
            else:
                prob.append(float(a))
        # the prob list should now be made
        #print(prob) # DEBUG
        expected = []
        # three choices: keep typing, remove n char first, start again
        # ONE: keep typing
        ##expected.append(prod(prob,A)*(-B - 1) + (2*B - A + 2))
        # TWO: 0 <= n <= A
        for n in range(0,A+1):
            foo = prod(prob,(A-n))*(-B - 1) + (2*n + 2*B - A + 2) # fail, not n
            expected.append(foo)
        # THREE: just try again
        expected.append(2 + B)
        expected = sorted(expected) # increasing value
        outcome.write("Case #%d: %f" % (caseCount, expected[0]))
        if caseCount != total:
            outcome.write("\n")
        lineState = 1 # reset the counter for next case
        caseCount += 1
        #lineCount += 1
            
income.close()
outcome.close()
