import sys
import copy
from helper import *

def parse_case(file):
    return map(int, parse_string(file).split())

def solve(case, file):
    
    # Simulate a single snap
    def snap(snappers):
        # Go from left to right
        for i in xrange(0, len(snappers)):
            state = snappers[i]
            snappers[i] = not snappers[i]
            if not state:
                break
            
    # Parse case
    devices, snaps = parse_case(file)
    
    # Set up snappers
    snappers = [False for i in xrange(0, devices)]
    
    # Do the snaps
    for i in xrange(0, snaps):
        snap(snappers)
    
    # Check if light is on
    lighton = all(snappers)

    # Output result
    print 'Case #%s: %s' % (case, 'ON' if lighton else 'OFF')

def main():
    file = open_input()
    cases = int(file.readline())
    for case in xrange(1, cases+1):
        solve(case, file)

if __name__ == '__main__':
    main()