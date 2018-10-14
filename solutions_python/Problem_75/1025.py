f = open('B-small-attempt1.in','r')
lines=f.readlines()
T = int(lines[0] )
for i in range(1,T+1):
        combine=[]
        opposed=[]
        line=[x for x in lines[i].split()]
        #print(line)
        j=0
        k=0
        for j in range(1,int(line[0])+1):
            combine.append(line[j])
            #print(line[j])
        #print('j:',j)
        for k in range(j+2,j+2+int(line[j+1])):
            #print(line[k])
            opposed.append(line[k])
        #print(combine)
        #print(opposed)
        s=[x for x in line[len(line)-1]]
        #print(s)
        n=len(s)
        opposed_state=[-1 for x in opposed]
        opposed_used=[-1 for x in opposed]
        for j in range(0,n):
            #print('j:',j)
            for k in range(0,len(opposed)):
                o=[x for x in opposed[k]]
                if(s[j]==o[0] and opposed_used[k]==1):
                    for l in range(0,j+1):
                        s[l]=' '
                    opposed_state[k]=-1
                    opposed_used[k]=-1
                    break
                elif(s[j]==o[1] and opposed_used[k]==0):
                    for l in range(0,j+1):
                        s[l]=' '
                    opposed_state[k]=-1
                    opposed_used[k]=-1
                    break
            if(s[j]==' '):
                continue
            if(j==n-1):
                break
            for c in combine:
                c=[x for x in c]
                #print(c)
                if(c[0]==s[j] and c[1]==s[j+1]):
                    s[j]=' '
                    s[j+1]=c[2]
                    break
                if(c[1]==s[j] and c[0]==s[j+1]):
                    s[j]=' '
                    s[j+1]=c[2]
                    break
            if(s[j]==' '):
                continue
            for k in range(0,len(opposed)):
                o=[x for x in opposed[k]]
                #print(s[j],o)
                if(s[j]==o[0] and opposed_state[k]==-1):
                    #print("going to remove",o,"0")
                    opposed_state[k]=j
                    opposed_used[k]=0
                elif(s[j]==o[1] and opposed_state[k]==-1):
                    #print("going to remove",o,"1")
                    opposed_state[k]=j
                    opposed_used[k]=1
            #print(s)
        #print(s)
        try:
            while(1):
                s.remove(' ')
        except ValueError:
            a=1
        if(len(s)>0):
            result="["
            for j in range(0,len(s)-1):
                result+=s[j]+", "
            result+=s[len(s)-1]+"]"
        else:
            result="[]"
        print("Case #%d: %s"%(i,result))
