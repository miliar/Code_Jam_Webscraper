t=int(raw_input())
for m in range(0,t):
    x=int(raw_input())
    h=str(x)
    flag=0
    count=1
    for i in range(1,len(h)):
        if(int(h[i-1])>int(h[i])):
            if(h[i]=='0'):
                if(h[:i].count('1')==i):
                    print "Case #"+str(m+1)+": "+"".join(['9']*(len(h)-1))
                elif(h[:i].count(h[i-1])==i):
                    print "Case #"+str(m+1)+": "+str(int(h[i-1])-1)+str(int("".join(['9']*(len(h)-1))))
                else:
                    print "Case #"+str(m+1)+": "+str(int(h[:i])-1)+str(int("".join(['9']*(len(h)-i))))
                flag=1
                break
            else:
                if(h[:i].count(h[i-1])==i):
                     print "Case #"+str(m+1)+": "+str(int(h[i-1])-1)+str(int("".join(['9']*(len(h)-1))))
                else:
                    print "Case #"+str(m+1)+": "+str(int(h[:i])-1)+str(int("".join(['9']*(len(h)-i))))
                flag=1
                break
        else:
            count+=1
    if(count==len(h) and flag==0):
        print "Case #"+str(m+1)+": "+str(x)