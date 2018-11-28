#!/usr/bin/env python
# >

import sys

flag = 0
for line in file(sys.argv[1]):
    if flag == 0:
        ntests = int(line)
        flag = 1
        continue ;
    result = 0
    max_shy, payload = line.split(" ")
    max_shy = int(max_shy)
    shy_flag = 0

    for shy_lvl in payload[:-1]:
        shy_lvl = int(shy_lvl)
        if shy_flag == 0:
            if shy_lvl == 0:
                result += 1
            elif shy_lvl == 1:
                pass ;
            elif shy_lvl > 1:
                shy_flag += shy_lvl - 1 ;
        else:
            if shy_lvl == 0:
                pass ;
            elif shy_lvl >= 1:
                shy_flag += shy_lvl
            shy_flag -= 1
    print "Case #%d: %d" % (flag, result)
    flag += 1
