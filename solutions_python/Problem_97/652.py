# -*- coding: utf-8 -*-
import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')
input_file.readline()

for i, s in enumerate(input_file.readlines()):
    M, N = [ int(x) for x in s.split()]
    result = 0
    for x in xrange(M, N+1):
        str_x = str(x)
        usage = set()
        for ii in xrange(1, len(str_x)):
            str_r = str_x[ii:] + str_x[:ii]
            if str_r[0] != '0':
                r = int(str_r)
                if r > x and M <= r <= N and not r in usage:
                    result += 1
                    usage.add(r)

    output_file.writelines("Case #{0}: {1}\n".format(i+1, result))


