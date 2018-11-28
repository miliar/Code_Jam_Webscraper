import os
import sys

# Friends should always have shyness S_f=0
def a(filein, fileout='a_out.txt'):
    infile = open(filein, 'r')
    outfile = open(fileout, 'w')
    T = int(infile.readline())
    for t in range(T):
        s_max, shyness_string = infile.readline().split(' ')
        shyness = [int(c) for c in list(shyness_string[:-1])]
        standing = 0
        friends = 0
        for i,s in enumerate(shyness):
            if standing < i and s > 0:
                new_friends = i-standing
                friends += new_friends
                standing += new_friends
                
            standing += s

        outfile.write('Case #%d: %d\n' % (t+1, friends))

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if os.path.isfile(arg):
        a(arg)
