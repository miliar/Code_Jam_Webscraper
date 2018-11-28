#!/usr/bin/env python

#out = open('B-small-out.out', "w")

import math

if __name__ == '__main__':
    
    t  = int(raw_input())
    for case in xrange(1, t+1):
        p = int(raw_input())
        limits = map(int, raw_input().split(' '))
        costs = []
        tmp_p = p
        while tmp_p:
            costs.extend(map(int, raw_input().split(' ')))
            tmp_p -= 1
        costs.reverse()
        costs = [[value, False] for value in costs]
        costs.insert(0, "")
        result = 0
        cant = len(limits)
        while min(limits) < math.log(cant, 2):
            #print limits
            #print costs
            index = limits.index(min(limits)) + 1
            #print "min ind" + str(index)
            i = 1
            mini = 1
            maxi = len(limits)
            middle = len(limits) / 2
            while costs[i][1]:
                if index > middle:
                    i = (i * 2 + 1)
                    mini = middle + 1
                    middle = (mini + maxi) / 2
                else:
                    i = i * 2 
                    maxi = middle
                    middle = (mini + maxi) / 2
                #print str(index)  + " -- " + str(i)
            costs[i][1] = True
            result += costs[i][0]
            for ind in xrange(mini-1, maxi):
                limits[ind] += 1
        print "Case #%d: %d" % (case, result)
        
    