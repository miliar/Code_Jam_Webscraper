
def get_pairs(x, B):
    firstB = str(B)[0]
    strx = str(x)
    result = set()
    for cut in range(1, len(strx)):
        #print cut
        if strx[-cut] != '0' and strx[-cut] <= firstB:
            recycled = int(strx[-cut:] + strx[0:-cut])
            #print recycled
            if recycled > x and recycled <= B:
                result.add(recycled)
    #print result
    return len(result)

#print get_pairs(1234, 10000)
    
cases = int(raw_input())
for case in range(cases):
    A, B = map(int, raw_input().strip().split())
    result = 0
    for n in range(A, B + 1):
        result = result + get_pairs(n, B)
    print 'Case #%d: %d' % (case + 1, result)