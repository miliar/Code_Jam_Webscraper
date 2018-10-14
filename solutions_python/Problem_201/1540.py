#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python solve.py < input.txt > result.txt
def solve(nbr):
    n_and_k = nbr.split(" ")
    N = int(n_and_k[0])
    K = int(n_and_k[1])
    old_K = 1
    queue = [N]
    last = False
    #print float(N)/K
    while K > 0:
        #print "START QUE " + str(queue)
        i = 1
        while i < len(queue) and queue[i-1] == queue[i]:
            i += 1
        toilets = queue[0]
        queue=queue[i:]
        K -= i
        for x in range(i):
            if toilets % 2 == 0 and toilets > 0:
                queue.extend([toilets/2, toilets/2-1])
            else:
                queue.extend([int(toilets/2), int(toilets/2)])

        if K > 0:
            #queue=queue[:K]
            queue.sort(reverse=True);
        #print K
        #print "END QUE " + str(queue)
        #print sum(queue) + old_K
    return str(queue[-2])+" "+str(queue[-1])

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
