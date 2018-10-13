'''
Created on Apr 13, 2013

@author: friend1
'''
import math
import numpy
def diss(no):
    ret = 0
    while(no > 0):
        ret = (10 *ret)+(no%10)
        no//=10
    '''
    if (ret == no1):
        return True
    return False
    '''
    return ret

def comb (data):
    ssmall , slarge = data.strip().split(' ')
    small = int(ssmall)
    large = int(slarge)
    count = 0
    for no in xrange(small , large +1):
        ret = diss(no)
        ret2 = -1 
        if (ret == no):
            ret2 = numpy.sqrt(no)
            if (ret2 == math.floor(ret2)):
                if (ret2 == diss(ret2)):
                    #print no 
                    count += 1
    return count

    
try:
    fin = open(r'in\C-small-attempt0.in','r')
    fout = open(r'out\C-small-attempt0.out','w')

    amount = int(fin.readline())
    
    for i in range(1,amount+1):
    
       
        fout.writelines('Case #'+str(i)+': '+str( comb(fin.readline()))+'\n')
        
        
finally:
    fin.close()
    fout.close()        
            