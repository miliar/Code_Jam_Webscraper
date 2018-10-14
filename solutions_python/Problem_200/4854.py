
def solve(n):
    numbers = []
    for number in str(n):
        numbers.append(number)
    if numbers == sorted(numbers):
        return(numbers)
    else:
        n = int(n)
        n -=1
        return(solve(n))
    
       


f = open("B-small-attempt0.in",'r')
output = open("B-small-attempt0.out",'w+')


a = 0
cs = 0
for line in f:
    i = 0
    found = False
    numbers = []
    cs += 1
    b = 0
    if a == 0:
        t = line
        a += 1
        cs -= 1
        b +=1
    else:
        n = line.replace('\n','')
        ans = ''.join(solve(n))
        output.write("Case #" + str(cs) + ": " + (ans)+'\n')
        

        
        
    
output.close()
        
        
