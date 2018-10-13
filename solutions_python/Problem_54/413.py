'''
Created on May 8, 2010

@author: Darren
'''

from fractions import gcd

if __name__ == "__main__":
    f = open("B-large.in", "r")
    fout = open("B-large.out", "w")
    # C, the number of test cases in the input file
    C = int(f.readline())
    for i in xrange(C):
        ts = [int(x) for x in f.readline().split()]
        N = ts.pop(0)
        ts.sort()
        largest_factor = ts[1]-ts[0]
        for j in xrange(2, len(ts)):
            largest_factor = gcd(largest_factor, ts[j]-ts[j-1])

        remainder = ts[0] % largest_factor
        result = 0 if remainder == 0 else largest_factor - remainder
#        print result
        fout.write(''.join(('Case #', str(i+1), ': ', str(result), '\n')))
    fout.close()
    f.close()