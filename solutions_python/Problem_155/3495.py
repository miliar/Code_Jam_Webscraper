## Google Code Jam contest!
# I need to read a file and save the results in other one.
# The first parameter is the input file name
import sys
import os

# chage: file_out.write  by print


pathfile = sys.argv[1]

file_in = open(pathfile, mode='r')
file_out = open('QA-problem-A-output.txt', mode='w')

# First line: number of cases
n_cases = int(file_in.readline())
# Followed by n_cases lines.

current_case = 0
while current_case < n_cases:
    current_case += 1
    this_case = file_in.readline().split()
    # maximum audence (audence is maximum+1 numbers)
    maximum = int(this_case[0])
    audience = [int(a) for a in this_case[1]]
    # DO THE STUFF
    friends = 0
    if len(audience) == 1:
        file_out.write('Case #{:d}: {:d}\n'.format(current_case, friends))
        continue
    people_standing = audience[0]
    for s, i in enumerate(audience[1:]):
        s += 1
        if i != 0:
            if people_standing >= s:
                people_standing += i
            else:
                friends += s-people_standing
                people_standing += friends + i
    
    file_out.write('Case #{:d}: {:d}\n'.format(current_case, friends))


file_in.close()
file_out.close()