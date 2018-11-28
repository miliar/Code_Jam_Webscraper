'''
Created on Apr 11, 2015

@author: Pango
'''

from os.path import basename
import re
import os
import bisect
import sys

sys.setrecursionlimit(100000)

DEBUGMODE = True

PMAX = 10
OPT_MAP = {}

### Functions ###
def debug(text):
    global DEBUGMODE
    if DEBUGMODE:
        print 'DEBUG:', text

def findFastest(p_ary):
    p_max = p_ary[-1]
    if p_max <= 3:
        return p_max # The answer when max(P_i) <= 3 is obvious
    else:
        # Now we need to find out!
        # 1 - Try eat
        p_ary_next = [elem -1 for elem in p_ary if elem > 1]
        counter1 = findFastest(p_ary_next)

        # 2 - Try Special(s)
        counter2 = -1
        global OPT_MAP
        move_num = OPT_MAP[p_max]
        #for move_num in range(1, p_max/2+1):
        p_ary_next = p_ary[:] # copy array
        p_ary_next.pop() # remove the p_max
        bisect.insort(p_ary_next, p_max - move_num)
        bisect.insort(p_ary_next, move_num)
        counter_tmp = findFastest(p_ary_next)
        if counter2 == -1 or counter2 > counter_tmp:
            counter2 = counter_tmp

        if counter1 > counter2:
            #debug('    %s>    SPECIAL %d vs (%d)' % (p_ary, counter1, counter2))
            return 1 + counter2
        else:
            #debug('    %s>    EATING (%d) vs %d' % (p_ary, counter1, counter2 ))
            return 1 + counter1

def solveOne(data1, data2):
    d = int(data1)
    p_ary = []
    for a in data2.split(' ', d):
        p_i = int(a)
        bisect.insort(p_ary, p_i) # User btree sort
    debug('input : %d, %s' % (d, str(p_ary)))

    return findFastest(p_ary)

### Main ###
if __name__ == '__main__':

    # Prepare
    for i in range(1, PMAX+1):
        counter = -1
        opt_val = i/2
        for j in range(i/2, 0, -1):
            OPT_MAP[i] = j
            counter_tmp = findFastest([i])
            if counter == -1 or counter > counter_tmp:
                counter = counter_tmp
                opt_val = j
        OPT_MAP[i] = opt_val

    filename = re.sub('\.py$', '', basename(__file__))

    input_filepath = './input/large/' + filename + '.dat'
    if not os.path.exists(input_filepath):
        input_filepath = input_filepath.replace('/large/', '/small/')
    if not os.path.exists(input_filepath):
        input_filepath = input_filepath.replace('/small/', '/sample/')
    output_filepath = input_filepath.replace('/input/', '/output/')

    with open(input_filepath) as fp:
        with open(output_filepath, 'w') as fpw:
            ln = fp.readline().rstrip()
            caseNumber = int(ln)
            for i in range(caseNumber):
                ln1 = fp.readline().rstrip()
                ln2 = fp.readline().rstrip()
                answer = 'Case #%d: %d' % ((i+1), solveOne(ln1, ln2))
                print answer
                fpw.write(answer + os.linesep)

