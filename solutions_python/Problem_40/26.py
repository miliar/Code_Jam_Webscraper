import re
f = open('A_1B.in', 'r')
out=open('A_1B.out','w')
n=int(f.readline()[:-1])

for qqq in range(1,n+1):
    lin=int(f.readline()[:-1])
    s=''
    for j in range(lin):
        s+=f.readline()[:-1]
    
    an = int(f.readline()[:-1])
    a=[]
    for j in range(an):
        a.append(f.readline()[:-1])
    
    a=[x.split() for x in a]
    a=[[x[0]]+[x[2:]] for x in a]
    s1=''
    for i in range(len(s)):
        if s[i]==')' or s[i]=='(':
            s1+=' '+s[i]+' '
        else:
            s1+=s[i]
    #print re.findall(r'[0-9\.]+|[^0-9\.]+', s)
    s=s1
    s=s.split()
    for x in range(len(s)):
        if '0' in s[x]:
            s[x]=float(s[x])

    for x in range(len(s)):
        break
    s=str(s)
    s=s.replace("'(', ",'[')
    s=s.replace(", ')'",']')
    s=eval(s)[0]
   
    #print s
    out.write("Case #"+str(qqq)+':\n')
    for animal in a:
        p=s[0]
        path=[]
        x=s
        while len(x)>=2:
            if x[1] in animal[1]:
                path.append(1)
                x=x[2]
            else:
                path.append(2)
                x=x[3]
            p*=x[0]
        out.write('%.8f'%p+'\n')
        