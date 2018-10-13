import time
import math

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

filename = "D-small-attempt0.in"

file = open(filename)
out=open(filename.replace("in","out"), 'w')

line_num = 0
cases = 0

line = file.readline()
cases = eval(line)
print 'Number of cases', cases

for case in range(cases):  
    print case + 1
    
    k = eval(file.readline().strip())

    input = file.readline().strip()
     
    print input 
     
    karray = []
    for x in xrange(k):
        karray.append(x+1)
        
    print 'karray', karray
    
    min_counter = 5000000
    
    for p in all_perms(karray):
        #print p,
        
        output = []
        j = 0
        while j < len(input):
            for i in xrange(k):
                output.append(input[j + p[i]-1])
            j += k
            
        #print output,
        
        counter=1
        z = 0
        while (z < len(output) - 1):
            if (output[z] != output[z+1]):
                counter += 1
                
            z += 1
                
        #print counter
        
        if counter < min_counter:
            min_counter = counter
        
    
    s ="Case #" + str(1+case) + ": " + str(min_counter)
    print s
    out.write(s + '\n')

    line_num += 1

file.close()
out.close()


