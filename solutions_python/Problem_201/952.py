'''
Created on 3/18/17

@author: junkang

'''
import sys
import heapq
from datetime import datetime

def loadInput(filename):
    input = []
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            input.append([int(n) for n in line.split()])

    print len(input)
    return input[1:]


def assign_stall(inp):
    """
    
    :param inp: [# of stalls, # of people] 
    :return: 
    """
    # print "inp",inp
    N = inp[0]
    K = inp[1]

    k = K
    ls = -1
    rs = -1

    dists = {N:1}
    while k > 0:
        d = max(dists.keys())

        ls = (d-1)/2
        rs = d/2

        # if dists[d] >= k:
        #     break
        # else:
        cnt = dists[d]
        dists.pop(d)
        k -= cnt
        if ls > 0:
            if ls not in dists:
                dists[ls] = 0
            dists[ls] += cnt
        if rs > 0:
            if rs not in dists:
                dists[rs] = 0
            dists[rs] += cnt
        # print dists


    return (str(max(ls, rs)), str(min(ls, rs))), dists



def saveOutput(outputs, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(outputs))
    print '- output:', filename

if __name__ == '__main__':
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_C/test.in', '/Users/junkang/Projects/codejam/qual_C/test.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_C/test2.in', '/Users/junkang/Projects/codejam/qual_C/test2.out'
    filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_C/C-large.in', '/Users/junkang/Projects/codejam/qual_C/C-large.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_C/C-small-2-attempt0.in', '/Users/junkang/Projects/codejam/qual_C/C-small-2-attempt0.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/qual_C/C-small-1-attempt0.in', '/Users/junkang/Projects/codejam/qual_C/C-small-1-attempt0.out'


    input = loadInput(filename_in)
    # input = []

    start = datetime.now()

    outputs = []
    for i, inp in enumerate(input):
        prev = datetime.now()
        ret, dist = assign_stall(inp)
        end = datetime.now()
        output = 'Case #%d: %s'%(i+1, ' '.join(ret))
        print '%15s => %s'%(inp, output), dist, '%s s'%(end - start)
        outputs.append(output)
    print 'Total elapsed_time: %s s'%(datetime.now()-start)




    saveOutput(outputs, filename_out)
