def flip(s,i):
   
    for j in range(k):
        if(s[i]=='+'):
            s[i]='-'
            i+=1
        else:
            s[i]='+'
            i+=1
            

t=input()
tt=1
while t:
    t=t-1
    input_= map(str,raw_input().split())
    s=list(input_[0])
    k=int(input_[1])
    count=0
    flag=0
    for i in range(len(s)):
        if(s[i]=='-'):
            if(i+k-1<=len(s)-1):
                #temp = s[i:i+k]
              
                flip(s,i)
                #res.append(temp)
                count+=1

    

    if(s.count('+')!=len(s)):
        flag=1

    if(flag==0):
        print "Case #%d: %d" %(tt,count)
       
    else:
        print "Case #%d: %s" %(tt,"IMPOSSIBLE")
    tt+=1
                               
            
    
            
            
    
