#!/usr/bin/python

import sys

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
    [D, N] = [int(x) for x in line.split()]
    D += 0.0
    initial_positions = []
    speeds = []
    times = []
    for i in range(N):
        line = f.readline().strip()
        [K,S] = [int(x) for x in line.split()]
        initial_positions.append( K )
        speeds.append( S )
        times.append( (D-K)/S )
    total_time = max(times)
    speed = D/total_time


    print "Case #" + str(case_num+1) + ":", speed

