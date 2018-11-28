import os
import math
   
def pal(number):
    string = str(number)
    return (string == string [::-1])

def sqr(n,m):
    start = int(math.ceil(math.sqrt(n)))
    stop = int(math.sqrt(m))+1
    for i in range(start, stop):
        if pal (i) and pal (i*i):
            yield (i*i)


def analyse(n,m):
    results = []
    result = 0
    for ans in sqr(n,m):
        results.append(ans)
        result +=1
    print (results)
    return result
        
    
filein = open ('C-small-attempt0.in', 'r') 
outfile = open ('sample.out', 'wt')
instances = int(filein.readline())

for i in range (instances):
    l = filein.readline()
    n,m = l.split()
    n = int(n)
    m = int(m)
    print (n,m)
    answer = analyse (n,m)
    stringStart = str('Case #' + str(i+1) + ': ')
    print(stringStart + str(answer) )
    outfile.write(stringStart + str(answer))
    outfile.write('\n')
filein.close()
outfile.close()
