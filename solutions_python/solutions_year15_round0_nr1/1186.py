__author__ = 'banarasitippa'

import sys
if len(sys.argv) < 3:
    print "usage :" + sys.argv[0] + "infile outfile"
    exit()
# open  input and output file
infile_name = sys.argv[1]
outfile_name = sys.argv[2]
infile = open(infile_name,'r')
outfile = open(outfile_name,'w')

# read number of test cases
testcases = int(infile.readline().strip())

# read test cases one by one
for test_no in range(testcases):
    line = infile.readline()
    S = line.split()
    shy_max = int(S[0])
    ppl_avl = 0
    stand_req = 0
    for ch in range(shy_max):
        members = int(ch)
        #increase the available standing people with next count
        ppl_avl += int(S[1][members])

        # if less than required then increase standing requests and adjust people available
        if ppl_avl < (members+1):
            stand_req += members+1 - ppl_avl
            ppl_avl = members+1

    dataline = "Case #" + str(test_no+1) + ": " + str(stand_req) + '\n'
    outfile.write(dataline)

outfile.close()
infile.close()