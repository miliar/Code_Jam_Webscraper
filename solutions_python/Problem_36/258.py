#!/usr/bin/python
import sys

input = sys.stdin
N = int(input.readline())
needle = "welcome to code jam"



def findneedle(needle, haystack):
    if len(needle) == 0:
        return 1
    else:
        sum = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                sum += findneedle(needle[1:], haystack[i:])
        return sum



for n in range(1,N+1):
    sys.stdout.write('Case #'+str(n)+': ')
    haystack = input.readline()

    haystack = haystack[haystack.find(needle[0]):haystack.rfind(needle[-1])+1]
    haystack = ''.join([x for x in haystack if x in needle])
    
    if len(haystack) < len(needle):
        sys.stdout.write('0000\n')
        continue

    ans = findneedle(needle, haystack)
    ans = int(str(ans)[-4:])
    sys.stdout.write(str(('%04d' % ans))+'\n')

