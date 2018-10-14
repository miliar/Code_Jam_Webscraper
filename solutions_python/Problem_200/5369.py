#!/usr/bin/python
# vim: ts=4 sw=4
import sys

case = 1
sys.stdin.readline()
for line in sys.stdin:
    num = list(line.rstrip())
    l = len(num)

    if (l > 1):
        pos=0
        i = 0
        while i < l-1:
            if num[i] > num[i+1]:
                num[pos] = str(int(num[pos]) - 1)
                # make rest of string 9s
                num[pos+1:] = ['9'] * (l - pos - 1)
                
            elif num[i] < num[i+1]:
                pos += 1
            i += 1


    tmp = str(int("".join(num)))
    
    #print 'Case #', case, ':', line
    #print 'Case #{}: {}'.format(case, line)
    print 'Case #' + str(case) + ':', tmp
    case += 1
