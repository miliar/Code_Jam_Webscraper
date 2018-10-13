import math
import gmpy


def palindrone(num):

    num2 = num[:]
    num2.reverse()
 
    return num == num2
def throughRange(low,high):
    count = 0
    for i in range(low,high+1):
        if( gmpy.is_square(i)):
        
            x = palindrone(list(str(i)))
            integer = math.sqrt(i)
            y = palindrone(list(str(int(math.sqrt(i)))))
 
            if(x and y ):

                count += 1

    return count
fname = 'C-small-attempt0'

f = open(fname+'.in')

lines = f.readlines()
f.close()
f = open(fname+'.out','w')
cases = int(lines[0])
lines.pop(0)

    

for i in range(1,cases+1):
    
    line = lines[0].strip().split(' ')
    lines.pop(0)
    low = int(line[0])
    high = int(line[1])
    count = throughRange(low,high)
    f.write("Case #{0}: {1}\n".format(i,count))
    
f.close()
