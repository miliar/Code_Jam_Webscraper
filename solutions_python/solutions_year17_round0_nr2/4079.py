t=input()
p=1
while p<t+1:
    n=raw_input()
    i=len(n)-1
    while i>0:
        if n[i]<n[i-1]:
            n=n[:i-1]+str(int(n[i-1])-1)+'9'*(len(n)-i)
        i-=1
    j=0
    while j<len(n):
        if n[0]=='0':
            n=n[1:]
        else:
            break
    print "Case #"+str(p)+": " +str(n)
    p+=1
  
