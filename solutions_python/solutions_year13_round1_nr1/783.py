'''
Created on 2013-4-27

@author: student
'''
import math
def main(args):
    problem, type = args[0], args[1]
    fin = "%s-%s-0.in" %(problem,type)
    fout = "%s-%s-0.out" % (problem,type)
    
    input = open(fin,'r')
    output = open(fout, 'w')
    
    T = int(input.readline())
    i = 1
    while i <= T:
        line = input.readline()
        args = line.split(' ')
        r, t = int(args[0]), int(args[1])
        
        y = 2*r - 1
        x = math.sqrt(y*y+8*t) - y
        m = x/4
        m = int(math.floor(m))
        
        while True:
            q = (2*m+y)*m-t
            if q > 0:
                m -= 1
            else:
                break
        output.write("Case #%s: %s\n"%(i,m))
        i += 1
    
    
    
    
    input.close()
    output.close()


main((1, "small"))