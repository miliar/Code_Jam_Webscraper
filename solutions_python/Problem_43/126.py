import math
import random
import re

if __name__ == '__main__':
    in_filename = "A-small.in"
    #in_filename = "A-dummy.in"
    #in_filename = "A-large.in"
    out_filename = "A-small.out"
    #out_filename = "A-large.out"

    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w')

    num_cases  = int(in_file.readline())

    for c in range(0,num_cases):
        s = in_file.readline()[:-1]
        min_base = len(list(set(list(s))))
        result = ''
        map = {}
        next = 0

        if min_base != 1:
            for i in range(0,len(s)):
                if i == 0:
                    result = result + '1'
                    map[s[i]] = '1'
                elif s[i] in map:
                    result = result + map[s[i]]
                else:
                    result = result + str(next)
                    map[s[i]] = str(next)
                    if next == 0:
                        next = 2
                    else:
                        next = next + 1
        else:
            result = '1'*len(s)
            min_base = 2
        l = list(result)
        dem = reduce(lambda x,y: x*min_base + y, [int(x) for x in l])
        print result, dem
        
        out_file.write("Case #%d: %d\n" % (c+1, dem))
    out_file.close()
