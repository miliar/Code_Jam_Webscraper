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

def convert_to_num( pancake ):
    if pancake == '+':
        return 0
    else:
        return 1

f = open( sys.argv[1] )

num_cases = int(f.readline().split()[0])

for case_num in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    [S, K] = line.split()
    K = int(K)
    S = [convert_to_num(x) for x in S]

    num_flips = 0
    for i in range(len(S)+1-K):
        #if ((S[i] == '+') and (num_flips%2 == 1)) or ((S[i] == '-') and (num_flips%2 == 0)):
        if S[i]%2 == 1:
            # We need to flip
            num_flips += 1
            for j in range(K):
                S[i+j] += 1
            #print "Flipping at", i

    # We've done what we have to do. Did the end end up OK?
    success = True
    for i in range(len(S)+1-K,len(S)):
        #if ((S[i] == '+') and (num_flips%2 == 1)) or ((S[i] == '-') and (num_flips%2 == 0)):
        if S[i]%2 == 1:
            success = False
            #print "Failing at", i

    if success:
        print "Case #" + str(case_num+1) + ":", num_flips
    else:
        print "Case #" + str(case_num+1) + ":", "IMPOSSIBLE"

