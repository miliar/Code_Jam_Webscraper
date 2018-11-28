# -*- coding: utf-8 -*-

"""
C. Theme Park
Qualification Round 2010
http://code.google.com/codejam/contest/dashboard?c=433101#s=p2

Mac OS X 10.6.3 (Build 10D573)
Python 2.5.4 (r254:67916, Feb 11 2010, 00:50:55) [GCC 4.2.1 (Apple Inc. build 5646)] on darwin

Cory Jacobsen <cory.jacobsen@gmail.com>
"""

# Import os for file path, and sys for input argument(s).
import os, sys

# From the given argument, read the file, save in var, close file.
f = open(os.path.join(os.path.dirname(__file__), sys.argv[1]), 'rb')
data = f.read().rstrip().lstrip().split('\n')
f.close()
result = ''

# Start algorithm.
#------------------------------------------------------------------------------

number_of_tests = int(data.pop(0))


for i in range(0, number_of_tests):
    temp = data.pop(0).split(' ')
    
    runs = int(temp[0])
    max_capacity = int(temp[1])
    groups = [int(x) for x in data.pop(0).split(' ')]
    place_index = 0
    euros = 0
    
    for j in range(0, runs):
        current_capacity = 0
        count = 0
        while count != len(groups):
            if place_index == len(groups):
                place_index = 0
            
            temp = current_capacity + groups[place_index]
            if temp <= max_capacity:
                current_capacity = temp
                place_index += 1
            
            count += 1
        
        euros += current_capacity
        
    result += 'Case #%d: %d\n' % (i+1, euros)
            
    

#------------------------------------------------------------------------------
# End algorithm.

# Clean up the result.
result = result.rstrip().lstrip()

# Either save the result to an output file or print it for testing
if len(sys.argv) > 2 and sys.argv[2] is not None:
    f = open(os.path.join(os.path.dirname(__file__), "%s.out.txt" %(sys.argv[1].split('.')[0])), 'w')
    f.write(result)
    f.close()
else:
    print result
