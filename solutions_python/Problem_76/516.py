def CANDY():
    testcases = int(raw_input())
    for cases in xrange(1,testcases+1):
        candies = int(raw_input())
        values = [ int(s) for s in raw_input().split()]
        result = 0
        for value in values:
            result = result ^ value
        if result == 0:
            print 'Case #' + str(cases) + ': ' + str(sum(values)-min(values))
        else:
            print 'Case #' + str(cases) + ': NO'
            
CANDY()


    
