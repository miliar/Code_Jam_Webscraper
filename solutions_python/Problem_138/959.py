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

for i in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    split_line = line.split()
    if len(split_line) != 1:
        print "Parsing error!"
    num_blocks = int(split_line[0])
    Naomi_blocks = [float(x) for x in f.readline().strip().split()]
    Ken_blocks = [float(x) for x in f.readline().strip().split()]
    if len(Naomi_blocks) != num_blocks or len(Ken_blocks) != num_blocks:
        print "Parsing error!"

    Naomi_blocks.sort()
    naive_Naomi_blocks = Naomi_blocks[:]
    Ken_blocks.sort()
    naive_Ken_blocks = Ken_blocks[:]
    
    Naomi_points = 0

    for j in range(num_blocks):
        if Naomi_blocks[0] < Ken_blocks[0]:
            # REMOVE FIRST ELEMENT FROM Naomi_blocks
            Naomi_blocks.pop(0)
            # REMOVE LAST ELEMENT FROM Ken_blocks
            Ken_blocks.pop()
        else:
            # REMOVE FIRST ELEMENT FROM_Naomi_blocks
            Naomi_blocks.pop(0)
            # REMOVE FIRST ELEMENT FROM Ken_blocks
            Ken_blocks.pop(0)
            Naomi_points += 1

    naive_Naomi_points = 0

    for j in range(num_blocks):
        if naive_Naomi_blocks[-1] < naive_Ken_blocks[-1]:
            # REMOVE LAST ELEMENT FROM BOTH
            naive_Naomi_blocks.pop()
            naive_Ken_blocks.pop()
        else:
            # REMOVE LAST ELEMENT FROM Naomi_blocks
            naive_Naomi_blocks.pop()
            # REMOVE FIRST ELEMENT FROM Ken_blocks
            naive_Ken_blocks.pop(0)
            naive_Naomi_points += 1

    print "Case #" + str(i+1) + ":", Naomi_points, naive_Naomi_points

