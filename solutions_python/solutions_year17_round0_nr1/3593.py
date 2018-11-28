t= int(raw_input())
m=1
while m<=t:
    f=0
    k=raw_input().split()
    s=k[0]
    n=int(k[1])
    print "Case #"+str(m)+":",
    l=len(s)
    st=[]
    for i in s:
        if i=='+':
            st.append(1)
        else:
            st.append(-1)
    tot=0
    #print st
    for i in range(l-n+1):
        if st[i]==-1:
            for j in range(i,i+n):
                st[j]=st[j]*-1
            tot+=1
            #print st
    for j in range(l-n,l):
        if st[j]==-1:
            print "IMPOSSIBLE"
            m=m+1
            f=1
            break
    if f:
        continue
    print tot
    m=m+1

