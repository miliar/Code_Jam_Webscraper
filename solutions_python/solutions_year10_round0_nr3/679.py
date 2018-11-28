'''
Created on 08 Mei 2010

@author: firman
'''
from array import array


if __name__ == '__main__':
    fin = open("C-small-attempt0.in","r")
    fout = open("C-small-attempt0.out","w")
    T = int(fin.readline());
    
    for i in range(1,T+1) :
        line = fin.readline().split(" ")
        R = int(line[0])
        k = int(line[1])
        N = int(line[2])
        d = 0
        
        p = fin.readline()[:-1].split(" ")
        
        a =array('i')
        for x in p: a.append(int(x))

        #"""
        
        num  = 0
        
        first_queue = 0
        for r in range (R):
            single_d = 0
            for m in range (N) :
                num= (first_queue + m)%N
                if (single_d + a[ num ] <= k ) :
                    single_d = single_d +a [num]
                else :
                    first_queue = num
                    
                    break
            d += single_d
            
        #print "Case #%s: %s\n"%(i,d)
        fout.write("Case #%s: %s\n"%(i,d))
        
        
        
            
    
    fin.close()