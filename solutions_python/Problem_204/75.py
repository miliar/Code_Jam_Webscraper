import sys
import itertools
import math

def solve(N, P, reqs, ings):
    #print N
    #print P
    #print reqs
    #print ings
    for i in range(0, N):
        for j in range(0, P):
            ings[i][j] = find_range(float(ings[i][j]) / reqs[i])

    for i in range(0, N):
        ings[i].sort()
    #print ings
    
    perms = itertools.permutations('12345678', 8)
    answer = 0
    #print N
    while len(ings[0]) > 0:
        if ings[0][0][1] == -1:
            del ings[0][0]
            continue
        success = 1
        for j in range(1,N):

            while len(ings[j]) > 0 and ings[j][0][0] == -1:
                #print len(ings[j])
                del ings[j][0]
            while len(ings[j]) > 0 and ings[0][0][0] > ings[j][0][1]:
                del ings[j][0]

            if len(ings[j]) <= 0:
                success = 0
                continue
            if ings[0][0][1] < ings[j][0][0]:
                success = 0
                continue

        if success == 1:
            for j in range(1, N):
                del ings[j][0]
        answer += success
        del ings[0][0]
            
    '''
    for i in perms:
        count = 0
        for j in range(0, P):
            if valid_pair(ings_new[0]
    '''
    return answer

def find_range(serv):
    low_start = math.ceil(serv)
    high_start = math.floor(serv)
    low = low_start
    high = high_start
    while low >= 1 and serv/low <= 1.1:
        low -= 1
    
    while high == 0 or serv/high >= 0.9:
        high += 1
    low = low+1
    high = high - 1
    if low > serv and high > serv:
        low = high
    if low < serv and high < serv:
        high = low
    if low > serv and high < serv:
        high = -1
        low = -1
    return [low,high]
    
    
    
#in_file = open("input.txt", 'r')
#in_file = open("B-small-attempt0.in", 'r')
in_file = open("B-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()
    N = int(line[0])
    P = int(line[1])
    line = in_file.readline().strip().split()
    reqs = []
    for i in range(0, N):
        reqs.append(int(line[i]))
    ings = []
    for i in range(0, N):
        ings.append([])
        line = in_file.readline().strip().split()
        for j in range(0,P):
            ings[i].append(int(line[j]))
            
        
    sol = solve(N, P, reqs, ings)

    answer = "Case #" + str(case) + ": " + str(sol) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

