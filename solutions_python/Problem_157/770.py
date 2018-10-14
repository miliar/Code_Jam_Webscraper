#!/usr/bin/env python

import sys

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
T = int(line)

# quaternion multiplication table
elts = ['1','-1','i','-i','j','-j','k','-k']
indices = range(8)
f = dict(zip(elts,indices))
g = {v:k for k,v in f.items()} # f-inverse
m = [[0]*8 for i in xrange(8)]
table = """1   -1  i   -i  j   -j  k   -k 
-1  1   -i  i   -j  j   -k  k
i   -i  -1  1   k   -k  -j  j
-i  i   1   -1  -k  k   j   -j
j   -j  -k  k   -1  1   i   -i
-j  j   k   -k  1   -1  -i  i
k   -k  j   -j  -i  i   -1  1
-k  k   -j  j   i   -i  1   -1"""
for i,row in enumerate(table.split('\n')):
    m[i] = map(lambda x: f[x],row.strip().split())

# convert to string
def mkstring(z):
    return "".join(map(lambda x: g[x], z))

def result(X,s):
    y = map(lambda x:f[x],s*X)
    n = len(y)
    # print mkstring(y)

    p = y[0]
    iloc = [] # product of y[:i] evaluates to i 
    jloc = [] # product of y[:j] evaluates to k 
    if y[0] == f['i']:
        iloc.append(1)
    for s in xrange(1,n):
        p = m[p][y[s]] # multiplication
        if g[p] == 'i':
            iloc.append(s+1)
        if g[p] == 'k':
            jloc.append(s+1)
    # for i in iloc:
    #     print "i:\t" + str(i) +  '\t' + mkstring(y[:i])
    # for i in iloc:
    #     for j in jloc:
    #         if i<j:
    #             print 'j:\t' + str(i) + ',' +  str(j) + '\t' +  mkstring(y[i:j])
    if g[p] == '-1' and len(iloc) > 0 and len(jloc) > 0 and max(jloc) > min(iloc):
        return "YES"
    else:
        return "NO"

# main method
def main():
    # process each case
    for t in xrange(0,T):

        # read case
        L, X = map(int, input_file.readline().strip().split())
        s = input_file.readline().strip()

        # print report
        print "Case #%d: %s" % (t+1,result(X,s))


if __name__ == '__main__':
    main()
