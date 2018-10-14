ip=open('input.txt','r')
op=open('output.txt','w')
for i in range(int(ip.readline())):
    s,k=ip.readline().split()
    k=int(k)
    count=0
    for j in range(len(s)-k+1):
        if s[j]=='+':
            pass
        else:
            count+=1
            for l in range(j,j+k):
                if s[l]=='+':
                    s=s[:l]+'-'+s[l+1:]
                else:
                    s=s[:l]+'+'+s[l+1:]
    if '-' in s:
        op.write("Case #"+str(i+1)+": "+"IMPOSSIBLE"+'\n')
    else:
        op.write("Case #"+str(i+1)+": "+str(count)+'\n')
            
ip.close()
op.close()
