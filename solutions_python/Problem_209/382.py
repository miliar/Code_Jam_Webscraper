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
    [N, K] = line.split()
    [N, K] = [int(N), int(K)]
    R = []
    H = []
    side_sa = []
    for i in range(N):
        line = f.readline().strip()
        [Ri,Hi] = [int(x) for x in line.split()]
        R.append(Ri)
        H.append(Hi)
        side_sa.append(2*math.pi*Ri*Hi)

    best_so_far = 0
    for i in range(N):
        # Assume bottom
        area = R[i]*R[i]*math.pi
        total_side_sa = side_sa[i]
        other_side_sas = []
        for j in range(N):
            if i != j:
                other_side_sas.append(side_sa[j])
        other_side_sas.sort()
        other_side_sas= other_side_sas[::-1]
        for j in range(K-1):
            total_side_sa+= other_side_sas[j]
        sa = total_side_sa + area
        #print "Bottom of radius", R[i], "gives answer of", sa
        if sa > best_so_far:
            best_so_far = sa



    print "Case #" + str(case_num+1) + ":", "%0.9f" % best_so_far

