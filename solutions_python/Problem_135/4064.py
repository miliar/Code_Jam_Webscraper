#!/usr/bin/python
import sys
def read_int(f):
    return int(f.readline().strip())
def get_candidates(f):
    """
    Expects first line to have the selected row the next 4 lines to have arrangement. Returns a set of candidates
    """
    selected_answer = read_int(tcases_file)
    for j in range(1,5):
        if j == selected_answer:
            candidates = set(map(lambda x:int(x),tcases_file.readline().strip().split()))
        else:
            tcases_file.readline()
    return candidates
tcases_file = open(sys.argv[1])
ncases = read_int(tcases_file)
for i in range(1,ncases+1):
    first_candidates = get_candidates(tcases_file)
    second_candidates = get_candidates(tcases_file)
    intersection = first_candidates.intersection(second_candidates)
    l_intersection = len(intersection)
    if l_intersection == 0:
        op = "Volunteer cheated!"
    elif l_intersection == 1:
        op = str(intersection.pop())
    else:
        op = "Bad magician!"
    print "Case #%d: %s" % (i,op)
