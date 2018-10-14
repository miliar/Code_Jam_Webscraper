from __future__ import print_function
from math import floor

# Fernando Gonzalez del Cueto. Code Jam 2017
from array import array
from collections import Counter

#infile = 'test.in'
#infile = 'C-small-1-attempt0.in'
infile = 'C-large.in'
outfile = infile.replace('.in', '.out')

fid = open(infile, 'r')

n_cases = int(fid.readline().strip())

def ins_sort(l):
    for i in range(1, len(l)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
        while j > 0 and l[j] < l[j-1]: #j>0 bcoz no point going till k[0] since there is no value to its left to be swapped
            l[j], l[j - 1] = l[j - 1], l[j] #syntactic sugar: swap the items, if right one is smaller.
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
    return l

class Bath(object):

    def __init__(self, n):

        self.segments = Counter({n:1})

    def enter(self, people):

        while people>0:

            #seg = max([size for (size, count) in self.segments.iteritems() if count>0])
            seg = max(self.segments)

            l_s = (seg-1)//2
            r_s = seg-l_s-1

            m = min(self.segments[seg], people)

            self.segments[seg] -= m
            if self.segments[seg]== 0:
                del self.segments[seg]

            self.segments[l_s] += m
            self.segments[r_s] += m

            people -= m

        return (l_s, r_s)


f_out = open(outfile, 'w')

for i_case in range(n_cases):

    n, k = [int(s) for s in fid.readline().strip().split()]

    b = Bath(n)

    l_s, r_s = b.enter(k)

    l = 'Case #%i: %i %i\n' % (i_case + 1, r_s, l_s)
    f_out.write(l)
    print(l, end='')

f_out.close()