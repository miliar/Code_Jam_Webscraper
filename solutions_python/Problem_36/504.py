N = int(raw_input())
cases = [raw_input() for x in xrange(N)]

needle="welcome to code jam"
#needle="jam"

def findString(haystack, haystackPos=0, needlePos=0):
    if haystackPos >= len(haystack):
        return 0
    if needlePos == len(needle) -1 and haystack[haystackPos] == needle[needlePos]:
        return 1 + findString(haystack, haystackPos+1, needlePos)
    numberOfNeedles=0
    if haystack[haystackPos] == needle[needlePos]:
        '''if needlePos == len(needle)-1:
            #Got full needle
            return numberOfNeedles+1'''
        numberOfNeedles += findString(haystack, haystackPos+1, needlePos)
        needlePos += 1
    numberOfNeedles += findString(haystack, haystackPos+1, needlePos)
    return numberOfNeedles

for index, case in enumerate(cases):
    print 'Case #%d: %04d' % (index+1, findString(case) % 10000)
#print findString('wweellccoommee to code qps jam')
