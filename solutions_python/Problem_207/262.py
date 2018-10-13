#!/usr/bin/python

import sys
import math

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
    [N, R, O, Y, G, B, V] = [int(x) for x in line.split()]
    #print "N was", N

    possible = True
    if R > N/2 or Y > N/2 or B > N/2:
        possible = False

    sorted_counts = sorted([R,Y,B])
    bigval = sorted_counts[2]
    litval = sorted_counts[0]
    medval = sorted_counts[1]

    # We assume that we are all bigs and mediums
    answer = []
    while len(answer) < N:
        answer.append('b')
        if len(answer) < N:
            answer.append('m')
    # Number big to overwite
    extra_b = N/2 - bigval
    if (N%2) == 1:
        extra_b += 1
    # Number med to overwrite
    extra_m = N/2 - medval
    # Check!
    if extra_b + extra_m != litval:
        print "Problem!!!!!"
        print "extra_b was ", extra_b
        print N
        print int(math.ceil(N/2)), " - ", bigval
        print "extra_m was ", extra_m
        print "litval was ", litval 

    for i in range(extra_b):
        answer[i*2] = 'l'
    for i in range(extra_m):
        answer[extra_b*2 + 1 + 2*i] = 'l'

    answer = "".join(answer)
    if "ll" in answer or "bb" in answer or "mm" in answer or answer[0] == answer[-1]:
        possible = False
    else:
        if R == bigval and Y == litval:
            answer = answer.replace('b','R')
            answer = answer.replace('l','Y')
            answer = answer.replace('m','B')
        elif R == bigval and B == litval:
            answer = answer.replace('b','R')
            answer = answer.replace('l','B')
            answer = answer.replace('m','Y')
        elif Y == bigval and B == litval:
            answer = answer.replace('b','Y')
            answer = answer.replace('l','B')
            answer = answer.replace('m','R')
        elif Y == bigval and R == litval:
            answer = answer.replace('b','Y')
            answer = answer.replace('l','R')
            answer = answer.replace('m','B')
        elif B == bigval and R == litval:
            answer = answer.replace('b','B')
            answer = answer.replace('l','R')
            answer = answer.replace('m','Y')
        elif B == bigval and Y == litval:
            answer = answer.replace('b','B')
            answer = answer.replace('l','Y')
            answer = answer.replace('m','R')
   
    if not possible:
        answer = "IMPOSSIBLE"
    
    #Runicorns = ["R" for x in range(R)]
    #Yunicorns = ["Y" for x in range(Y)]
    #Bunicorns = ["B" for x in range(B)]




    print "Case #" + str(case_num+1) + ":", answer

