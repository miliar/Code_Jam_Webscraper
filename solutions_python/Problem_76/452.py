def solve(n, c):

    if reduce(lambda x, y: x^y, c) != 0:
        return 'NO'    
    else:
        return reduce(lambda x, y: x+y, sorted(c)[1:])

#reduce(lambda x, y: x^y, a)
                
input = open('C-large.in', 'r')
output = open('candy.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
   
    n = int(input.readline())
    c = map(int, input.readline().split())
    
    #print n, c    
    result = solve(n, c)

    print 'Case #'+str(case)+':', result
    #print
    output.write("Case #%s: %s\n" %(case, result))
