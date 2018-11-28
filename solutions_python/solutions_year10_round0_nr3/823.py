import sys
from helper import *

def parse_ints(file):
    return map(int, parse_string(file).split())

def solve(case, file):

    # Parse case
    totalruns, capacity, _ = parse_ints(file)
    groups = parse_ints(file)
    
    # Simulate
    euros = 0
    pos = 0
    riders = 0
    runs = 0
    lastrunat = 0
    while runs < totalruns:
        groupfits = groups[pos] + riders <= capacity
        if groupfits:
            riders += groups[pos]
            pos = (pos + 1) % len(groups)
            
        if not groupfits or pos == lastrunat:
            lastrunat = pos
            euros += riders
            riders = 0
            runs += 1

    # Output result
    print 'Case #%s: %s' % (case, euros)

def main():
    file = open_input()
    cases = int(file.readline())
    for case in xrange(1, cases+1):
        solve(case, file)

if __name__ == '__main__':
    main()