import numpy
f = open('3.ex', 'r')
fo = open('3.out' ,'w')

cases = int(f.readline())

for c in xrange(cases):
    
    begin, end = [int(x) for x in f.readline().split()]
    
    found = 0
    
    x = begin
    while x <= end:
        numstr = str(x)
        numstr_reverse = numstr[::-1]
        if numstr == numstr_reverse:
            sqrt = numpy.sqrt(x)
            sqrt = int(numpy.round(sqrt, 0))
            if sqrt*sqrt == x:
                sqrtstr = str(sqrt)
                sqrtstr_reverse = sqrtstr[::-1]
                if sqrtstr == sqrtstr_reverse:
                    found += 1
        x += 1
    print(str(c) + '/' + str(cases))
    
    output = str(found)
    
    fo.write('Case #' + str(c+1) + ': ' + str(output) + '\n')