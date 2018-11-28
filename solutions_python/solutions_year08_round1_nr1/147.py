# ------------------------------------------------------------------------------
# Google Code Jam 2008
#
# Author: Ademilson <ademilsonfp@gmail.com>
# Language: Python - http://python.org
# ------------------------------------------------------------------------------

numcases = int(raw_input())
case = 1

while case <= numcases:
    numcoords = int(raw_input())
    
    v1 = [int(j) for j in raw_input().split(' ')]
    v2 = [int(j) for j in raw_input().split(' ')]
    
    v1.sort()
    v2.sort()
    v2.reverse()
    
    prod = 0
    
    for i in range(numcoords):
        prod += v1[i] * v2[i]
    
    print 'Case #%d: %d' % (case, prod)
    
    case += 1