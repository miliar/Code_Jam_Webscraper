testcases=input()

def flip(s,i,m):
    temp=''
    for j in range(i,i+m):
        if s[j]=='-':
            temp=temp+'+'
        else:
            temp=temp+'-'
    if i==0:
        s=temp+s[i+m:]
    else:
        s=s[0:i]+temp+s[i+m:]
    return s


for t in range(testcases):
    p,k=raw_input().split(' ')
    counter=0
    try:
        for i in range(len(p)):
            if p[i]=='-':
                p=flip(p,i,int(k))
                counter=counter+1
            else:
                pass
    except:
        print("Case #"+str(t+1)+': '+'IMPOSSIBLE')
        continue
    print("Case #"+str(t+1)+': '+str(counter))
    




