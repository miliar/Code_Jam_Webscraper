from math import*
def check_palindrome(x):
    l=list(str(x))
    
    c=0
    m=0
    for i in range((len(l)/2)+1):
        c=c+1
        if l[i]==l[-(i+1)] :
            m=m+1
    if c==m :
        return 1
    else :
        return 0





def find_root(x):
    root=int(sqrt(x))
    if root*root == x :
        return root
    else :
        return -1
    




def solve(a,b) :
    
    c=0
    for i in range(a,b+1):
        if check_palindrome(i) and check_palindrome(find_root(i)) :
            c=c+1

    return c

    








f=open("answers_fair_pal.txt","w")

t=int(raw_input())
for i in range(t) :
    
    
    x=raw_input();
    tmp=x.split()
    #print "Case #"+str(i+1)+": "+solve(tmp)
    f.write("Case #"+str(i+1)+": "+str(solve(int(tmp[0]),int(tmp[1])))+"\n")

   


f.close()
    


        
    
