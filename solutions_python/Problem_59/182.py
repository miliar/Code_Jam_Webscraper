#!/usr/bin/python

"""
File Fix-it problem solution
(GCJ 2010, Round 1B)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: file_fixit.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

#filesystem emulation
def mkdir(path):
    global filesystem
    mkdirs_num = 0
    levels = len(path.split("/"))-1
    for i in range(levels):
        if path not in filesystem:
            filesystem.append(path)
            mkdirs_num += 1
        path = path[:path.rfind("/")]
    return mkdirs_num

# begin prosessing cases
for cur_case in range(T):
    # get constants
    N, M = map(int, in_file.readline().split(" "))
    # build existing directories list
    filesystem = []
    for i in range(N):
        mkdir(in_file.readline().strip())
    # calculate mkdirs needed
    mkdirs_num = 0
    for i in range(M):
        mkdirs_num += mkdir(in_file.readline().strip())
    # output result
    print "Case #%d: %s" % (cur_case + 1, mkdirs_num)

# close input file
in_file.close()

    
        
