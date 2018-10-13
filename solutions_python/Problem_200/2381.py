ip=open('input.txt','r')
op=open('output.txt','w')
def tidy(s):
    for i in range(len(s)-1):
        if s[i+1]<s[i]:
            return 0
    return 1
#print(tidy('9999999999999'))
for i in range(int(ip.readline())):
    s=str(ip.readline())
    s=s[:-1]
    ans=s
    while not tidy(s):
        #print(s,tidy(s))
        for j in range(len(s)-1):
            if s[j+1]<s[j]:
                tail=''
                for k in range(len(s)-j-1):
                    tail+='9'
                s=s[:j]+str(int(s[j])-1)+tail
    #print(str(int(s)),int(s))
    op.write("Case #"+str(i+1)+": "+str(int(s))+'\n')
            
ip.close()
op.close()
