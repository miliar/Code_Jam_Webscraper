import sys
from itertools import product, combinations

basename  = sys.argv[0][0:-3]

#basename = basename + "-practice"
basename = "D-small-attempt6"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())



for case in range(1, test_cases+1):
    lookup = dict()
    K, N = [int(i) for i in input_file.readline().rstrip().split()]
    mykeys = input_file.readline().rstrip().split()
    chests = [str(i) for i in range(1, N+1)]

    lock = dict()
    storedkeys = dict()

    for c in chests:
        line = input_file.readline().rstrip().split()
        lock[c] = line[0]
        storedkeys[c] = line[2:]
    
    def solve(schests, smykeys):
        schests.sort(key=int)
        smykeys.sort(key=int)
        if (tuple(schests),tuple(smykeys)) not in lookup:
            canopen = [c for c in schests if lock[c] in smykeys]
            canopen.sort(key=int)
            locktypes = set(lock[c] for c in schests)
            alllocks = [lock[c] for c in schests]

            #print("Chests: " + ' '.join(c + '(' + lock[c] + ')' for c in schests))
            #print("Have keys " + ' '.join(smykeys))
            #print("Can open " + ' '.join(c + '(' + lock[c] + ')' for c in canopen))
            
            if len(canopen) == 0:
                #print("Can't open any lockers.")
                lookup[tuple(schests),tuple(smykeys)] = -1
            
            elif all( smykeys.count(key) >= alllocks.count(key) for key in locktypes):
                #print("Can open all!!")
                #print("Keys: " + ' '.join(smykeys))
                #print("Chests: " + ' '.join(c + "(" + lock[c] + ")" for c in schests))
                lookup[tuple(schests), tuple(smykeys)] = schests

            else:
                done = False
                for c in canopen:
                    #print("Trying to open " + c + '(' + lock[c] + ')')
                    newchests = schests[:]
                    newchests.remove(c)

                    newkeys = smykeys[:]
                    newkeys.remove(lock[c])
                    newkeys.extend(storedkeys[c])

                    attempt = solve(newchests, newkeys)
                    if attempt != -1:
                        lookup[tuple(schests),tuple(smykeys)] = [c] + attempt
                        done = True
                        break
                    #else:
                        #print("No dice.  Trying next one.")
                if not done:
                    lookup[tuple(schests),tuple(smykeys)] = -1
        return lookup[tuple(schests),tuple(smykeys)]

    
    sol = solve(chests, mykeys)
    if sol == -1:
        result = "IMPOSSIBLE"
    else:
        result = ' '.join(sol)


    print("Case #" + str(case) + ": " + result)
    output_file.write("Case #" + str(case) + ": " + result)
    if case < test_cases:
        output_file.write('\n')

