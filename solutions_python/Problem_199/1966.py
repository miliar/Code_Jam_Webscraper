def parsePancakes(s):
    pancakes = []
    for c in s:
        if (c == '+'):
            pancakes.append(1)
        elif c == '-':
            pancakes.append(-1)
        else:
            print "ERROR PARSING PANCAKES STRING"
    return pancakes

def flipPancakes(pancakes, flipper_size, position):
    for i in range(position, position + flipper_size):
        pancakes[i] *= -1
    return pancakes

#~ f_out = open('B-small-practice.out', 'w')

#f_in = open('B-large-practice.in')
#f_out = open('B-large-practice.out', 'w')

## The number of test cases
#~ f_in = open('B-small-practice.in')
f_in = open('A-small-attempt1 (1).in')
#~ f_out = open('A-large-practice.out', 'w')
#~ T = int(f_in.readline())
T = int(raw_input())

pancakes = parsePancakes("---+-++-")
#~ print pancakes

#~ print flipPancakes(pancakes, 3, 0)

for i in range(T):
    ## The pancakes string 
    a = ((raw_input()).strip()).split()
    pancakes = parsePancakes(a[0])
    flipper_size = int(a[1])
    
    ## Greedy method. 
    nrFlips = 0
    for k in range(0, len(pancakes) - flipper_size + 1):
        if (pancakes[k] == -1):
            pancakes = flipPancakes(pancakes, flipper_size, k)
            nrFlips += 1
    
    #~ print "after flipping, pancakes is ", pancakes
    solString = "Case #" + str(i+1) + ":  "
    if -1 in pancakes:
        print solString + "IMPOSSIBLE"
    else:
        print solString + str(nrFlips)
    #~ f_out.write(solString + '\n')
    ## The number of costumers
    #~ C = int(f_in.readline())
    
    #~ print "in this test case we have ", M, " milkshake flavors and ", C, " customers"
