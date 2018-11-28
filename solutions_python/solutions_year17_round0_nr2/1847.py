from __builtin__ import False

def get_tidy(no):
    no = list(str(no))
    no=map(int, no)
    
    i=len(no)-1
    
    while i>0:
        if no[i] < no[i-1]:
            no[i-1]-=1
            for x in range (i,len(no)):
                
                no[x]=9
        i-=1
    
    no=map(str,no)      
    return "".join(no).lstrip("0")
    

t = int(raw_input())
for i in xrange(1, t + 1):
    ans = None
    n = int(raw_input())


    print("Case #{}: {}".format(i, get_tidy(n)))
