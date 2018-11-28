'''
Created on Apr 14, 2012

@author: kevin
'''
from collections import Counter


def check_recycled_pair(a,b):
    
    
    
    # criteria checks
    if a > b:
        return False
    a=str(a)
    b=str(b)
    
    if len(a) != len(b):
        return False
    
#    if ("0" in a or "0" in b):
#        return False
    
    if (set(a) != set(b)):
        return False
    
    # Num digit must be equal
    counterA = Counter(a)    
    counterB = Counter(b)
    for key in counterA.keys():
        if (counterA[key] != counterB[key]):
            return False
    
    
    for i in range(len(b)):
        new_val = b[i:] + b[:i]        
        if (int(new_val) == int(a)):
            return True
    #print "no match: %s %s" %(a,b) 
    return False
        
    
        
    
   
#print check_recycled_pair(12345,100)
#print check_recycled_pair(12345,123456)
#print check_recycled_pair(12345,15671)
#print check_recycled_pair(12345,34512)


def get_num_recycle(start, end):
    counter = 0
    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            #print "%i:%i" %(i,j)
            
            if check_recycled_pair(i,j):                
                counter += 1
    return counter

#print get_num_recycle(1,9)
#print get_num_recycle(10,40)
#print get_num_recycle(100, 500)
#print get_num_recycle(1111,2222)

if __name__ == "__main__":
    #input_file = 'pb_3_test_input.txt'
    input_file = 'C-small-attempt0.in'
    f = open(input_file,'r')
    
    num_entries = int(f.readline())
    for i in range(num_entries):
        start, end = map(int, f.readline().split())
        num = get_num_recycle(start, end)
        print "Case #%i: %i" % (i+1, num) 
        