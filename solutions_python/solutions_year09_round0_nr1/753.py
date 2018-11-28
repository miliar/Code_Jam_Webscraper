'''
Google CodeJam - Qualification Round 2009
A. Alien Language

@author: Chris Hill
'''

import sys,re

fileName = sys.argv[1]

# Read in the lines from the input file
lines = []
for line in open(fileName).readlines():
    lines.append(line.strip())


# Read in the L, D, and N from the first
l, d, n = lines[0].split()

# Store the dictionary of alien terms
dictionary = lines[1:int(d) + 1]

# Store the test cases
cases = []
for line in lines[int(d) + 1:int(d) + int(n) + 2]:
    # Replace the open and closed parenthesis with brackets
    # to allow regular expressions.
    line = line.replace('(', '[')
    line = line.replace(')', ']')

    cases.append(line)

#print 'dictionary words:\n', dictionary
#print 'N test cases:\n', cases  
#print l, d, n

# Cycle through test cases, and run their regular 
# against the dictionary words
caseNumber = 1
for case in cases:
    count = 0
    regexp = re.compile(case)
    for word in dictionary:
        result = regexp.match(word)
        if result:
            count+=1
    print 'Case #' + str(caseNumber) + ': ' + str(count)
    caseNumber+=1