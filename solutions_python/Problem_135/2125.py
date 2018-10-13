#!/usr/bin/env python

import sys

def main():
    filename = sys.argv[1]
    sys.stdout = open(filename.replace('.in', '.out'), 'w')
    
    f = open(filename)
    cases = int(next(f))
    
    for i in xrange(1, cases + 1):
        answer = parse(f)
        print 'Case #{0}: {1}'.format(i, answer)
    
def get(f):
    row = int(next(f))
    arr = []
    for i in xrange(4):
        arr.append(next(f).strip().split(' '))
    return row, arr
        
def parse(f):
    row1, arr1 = get(f)
    row2, arr2 = get(f)
    
    overlap = set(arr1[row1 - 1]).intersection(arr2[row2 - 1])
    overlap_len = len(overlap)
    
    if overlap_len == 1:
        return overlap.pop()
    elif overlap_len > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'
        
if __name__ == '__main__':
    main()
    
    