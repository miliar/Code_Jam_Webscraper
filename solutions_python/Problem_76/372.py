import operator

f = open('c.in')
cases = int(f.readline())
case = 1
while (case <= cases):
    
    n = int(f.readline())
    task = f.readline()
    numbers = map(int,task.split(' '))
    #print numbers
    
    result = reduce(operator.xor, numbers)
    
    patricks_pile = min(numbers)
    seans_pile    = sum(numbers) - patricks_pile
    
        
    if (result==0):
        s=str(seans_pile)
    else:
        s="NO"
    
    print "Case #"+str(case)+": "+s    
                
    case += 1