#!/usr/bin/python

import sys
from operator import itemgetter

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def nchoosek( n, k ):
    #return factorial(n)/(factorial(k)*factorial(n-k))
    answer = 1
    for i in range(1,k+1):
        answer *= (n - (k - i))
        answer /= i
    return answer


f = open( sys.argv[1] )

num_cases = int(f.readline().split()[0])

for case_num in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    [N, Q] = [int(x) for x in line.split()]
    ranges = []
    speeds = []
    for i in range(N):
        [E, S] = [int(x) for x in f.readline().strip().split()]
        ranges.append(E)
        speeds.append(S)
    distances_table = [[] for x in range(N)]
    for i in range(N):
        distances_table[i] = [int(x) for x in f.readline().strip().split()]
    for i in range(Q):
        [U,V] = [int(x) for x in f.readline().strip().split()]

    distances = [distances_table[i][i+1]+0.0 for i in range(N-1)]

    # Time, range, speed
    options = [[0,0,1]]
    # As you go from stop n to stop n+1, you expand all the legitimate ways to get to n into ways to get to n+1 (there will either be one or two expansions)
    for i in range(N-1):
        new_options = []
        for option in options:
            # Use the current city's horse
            new_time = option[0] + distances[i]/speeds[i]
            new_range = ranges[i] - distances[i]
            if new_range >= 0:
                new_options.append([new_time, new_range, speeds[i]])
            # Try using the horse you rode in on
            new_time = option[0] + distances[i]/option[2]
            new_range = option[1] - distances[i]
            if new_range >= 0:
                new_options.append([new_time, new_range, option[2]])

        # You then want to discard extraneous ones by: sort by speed, then if the fastest one has a horse available that has just as much speed and stamina as any of the others, those can be discarded
        new_options.sort(key=itemgetter(0))
        positions_to_remove = []
        for i in range(1,len(new_options)):
            if new_options[0][1] >= new_options[i][1] and new_options[0][2] >= new_options[i][2]:
                positions_to_remove.append(i)
        positions_to_remove = positions_to_remove[::-1]
        for pos in positions_to_remove:
            new_options.pop(pos)

        options = new_options[:]


    print "Case #" + str(case_num+1) + ":", options[0][0]

