#!/usr/bin/env python

def get_set(row):
    row_set = set()
    for i in xrange(4):
        if i == row:
            row_set = set(raw_input().split())
        else:
            raw_input()
    return row_set


for case in xrange(1, int(raw_input())+1):
    set1 = get_set(int(raw_input())-1)
    set2 = get_set(int(raw_input())-1)
    common = set1.intersection(set2)
    size = len(common)
    print "Case #%d:" % case,
    if size == 1:
        print common.pop()
    elif size > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
        
