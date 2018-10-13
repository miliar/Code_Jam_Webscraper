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
    N = line

    # Find first index that needs to change
    change_index = N
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            change_index = i
            break

    if change_index < N:
        while (change_index > 0) and (N[change_index] == N[change_index-1]):
            change_index -= 1

    answer = [int(x) for x in N]
    if change_index < N:
        answer[change_index] -= 1
        for i in range(change_index+1,len(N)):
            answer[i] = 9
        if answer[0] == 0:
            answer = answer[1:]

    answer = "".join([str(x) for x in answer])


    print "Case #" + str(case_num+1) + ":", answer

