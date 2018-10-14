#! /usr/bin/env python

# Speaking in Tongues
# Code Jam 2012 Round 1 - Problem B
# Mark Sherman brazentone@gmail.com

import sys


# Does the actual work solving the problem
def do_case(case_num):
    line = fin.readline().split()
    contestants = int(line[0])
    surprises = int(line[1])
    p = int(line[2])
    scores = line[3:]
    contestant_data = []
    
    count = 0

    for i in range(contestants):
        contestant_data.append( make_node( int(scores[i]) , p ) )
    
    for i in contestant_data:
        if i[0]:
            count = count + 1
        else:
            if (i[1] >= p) and (surprises > 0):
                count = count + 1
                surprises = surprises - 1            
    
    fout.write( "Case #" + str(case_num) + ": " + str(count) + '\n' )

# Node format: 
#   0   "selected" in final count, 
#   1   surprise max score (0 if already selected, as it doesn't matter)
def make_node(score, p):
    max_score = calculate_triplet(score, False)
    if max_score >= p:
        return [True, 0]
    else:
        return [False, calculate_triplet(score, True)]

def calculate_triplet(total_score, is_surprise):
    max = 11
    min_offset = 1
    
    if is_surprise:
        min_offset = 2
        
    is_valid = False
    
    while max > 0 and (not is_valid) :
        max = max - 1
        is_valid = is_triplet_valid( total_score - max , max - min_offset)
        #print "max: " + str(max) + " valid: " + str(is_valid)
    return max

def is_triplet_valid(remaining_score, minimum):
    if minimum < 0:
        minimum = 0

    return remaining_score >= 2 * minimum
    

######################################################
# Setup stuff

OUTFILE = 'outfile'
    
fin = open(sys.argv[1], 'r')

fout = open(OUTFILE, 'w')

CASES = int(fin.readline()) 

for i in range(CASES):
    do_case(i+1)
    
    