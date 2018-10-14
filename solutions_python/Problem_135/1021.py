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
    first_guess = int(split_line[0])
    first_rows = []
    for j in range(4):
        line = f.readline().strip()
        split_line = line.split()
        if len(split_line) != 4:
            print "Parsing error!"
        first_rows.append( split_line )
    line = f.readline().strip()
    split_line = line.split()
    if len(split_line) != 1:
        print "Parsing error!"
    second_guess = int(split_line[0])
    second_rows = []
    for j in range(4):
        line = f.readline().strip()
        split_line = line.split()
        if len(split_line) != 4:
            print "Parsing error!"
        second_rows.append( split_line )

    # Only a small set, so no need to be efficient here!
    first_card_options = first_rows[first_guess-1]
    #print first_card_options
    second_card_options = second_rows[second_guess-1]
    #print second_card_options
    possibilities = set(first_card_options).intersection( second_card_options )    
    #print possibilities

    if len( possibilities ) == 0:
        print "Case #" + str(i+1) + ": Volunteer cheated!"
    elif len( possibilities ) == 1:
        print "Case #" + str(i+1) + ":", possibilities.pop()
    else:
        print "Case #" + str(i+1) + ": Bad magician!"
        

