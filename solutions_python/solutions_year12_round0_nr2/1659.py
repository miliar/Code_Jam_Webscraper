f = open('input.txt','r')
g = open('output.txt','w')

ntest = int(f.readline())

for i in range(ntest):
        st=(f.readline()).rstrip('\n')
        l=st.split()
        n=int(l[0])
        s=int(l[1])
        p=int(l[2])
        l=l[3:]
        j=0
        k=0
        while j<len(l):
                if int(l[j])>=(3*p-2):
                        k=k+1
                elif (int(l[j])>=(3*p-4)) and s>0 and int(l[j])>0:
                        s=s-1
                        k=k+1
                elif int(l[j])==0 and p==0:
                        k=k+1
                j=j+1
        
        
        g.write((''.join(['Case #',str(i+1),': ',str(k),'\n'])))
f.close()
g.close()
