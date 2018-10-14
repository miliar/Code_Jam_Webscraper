"""
Kaydhi, Google code Jam 2017
Problem B
"""
def check_tidy(list_n):
    tidy=True
    last_val=list_n[0]
    untidy_idx=0
    #print list_n
    for m in list_n[1:]:
        untidy_idx+=1
        #print(m,last_val)
        if m<last_val:
            tidy=False
            break
        last_val=m
    return tidy,untidy_idx
            
def last_tidy_number(n):
    tidy,idx= check_tidy(n)
    if tidy:
        #print 'tidy'
        return int(''.join(map(str,n)))
    else:
        while not tidy: 
            n[idx-1]=n[idx-1]-1
            for j in range(idx,len(n)):
                n[j]=9
            tidy,idx=check_tidy(n)
        return int(''.join(map(str,n)))
 
        
    
    
    
if __name__=='__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = [int(s) for s in raw_input()]  # read
        result=last_tidy_number(n)
        print("Case #{}: {}".format(i, result))
        
        
