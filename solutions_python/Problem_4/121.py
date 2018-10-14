

if True:
    filebase = 'A-large'
    input = file(filebase + '.in').read().split('\n')
    N = int(input[0])
    
    index = 1
    for i in range(N):
        n = int(input[index]); index += 1
        v1 = map(int,input[index].split(' ')); index += 1
        v2 = map(int,input[index].split(' ')); index += 1
        
        # print v1,v2
        v1.sort()
        v2.sort()
        v2.reverse()
        
        minimum = 1e10
        
        product = sum(map(lambda (x,y): x * y, zip(v1, v2)))
        minimum = product
        # print p1,p2
        
        output = 'Case #%d: %d' % (i+1, minimum)
        file(filebase + '.out','a').write(output + '\n')
        print output
        
        