#!/usr/bin/python

#!/usr/bin/python

import sys
from collections import deque

def run(filename):
    f = open(filename, "r")
    case_count = int(f.readline())
    for i in xrange(case_count):
        line = f.readline()
        result = process_case(parse_case(line))
        print('Case #%d: %s' % (i+1, result))
  
def process_case(case):
    n, s, p, t = case        
    correct_match = [point for point in t if point >= 3 * p - 2 or p == 0]
    almost_match = [point for point in t if point not in correct_match and point >= 3 * p - 4 and (p != 1 or point > 0)]
    
    return len(correct_match) + min(len(almost_match), s)
    
def parse_case(line):
    pieces = deque(line.split())
    n = int(pieces.popleft())
    s = int(pieces.popleft())
    p = int(pieces.popleft())
    t = []
    for i in xrange(n):
        t.append(int(pieces.popleft()))
    return (n, s, p, t)

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "Sample.in"

run(filename)
