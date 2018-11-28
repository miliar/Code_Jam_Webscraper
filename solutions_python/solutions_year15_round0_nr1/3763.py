#!/usr/bin/env python

import sys

f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])
for i in range(1, len_cases+1):
	nbmaxshy = int(cases[i][0])
        start = int(cases[i][2])
        result = 0
        if nbmaxshy == 0:
                print "Case #%d: 0" % (i)
        else:
                for j in range(3, nbmaxshy+3):
                        if start >= j-2 or int(cases[i][j])==0:
                                start += int(cases[i][j])
                                #print "%d OK" % int(j-2)
                        else:
                                result += (j-2)-start
                                start += int(cases[i][j]) + result
                                #print "%d Result inter %d" % (j-2,result)
                        if (j-2)==nbmaxshy:
                                print "Case #%d: %d" % ((i), result)
                # print int(cases[i][j])
	# if result != []:
	# 	if len(result) > 1:
	# 		print "Case #%d: Bad magician!" % int((i+9)/10)
	# 	else:
	# 		print "Case #%d: %s" % ((i+9)/10, result[0])
	# else:
	# 	print "Case #%d: Volunteer cheated!" % int((i+9)/10)
f.close()
