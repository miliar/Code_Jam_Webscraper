T=int(raw_input().strip())
for i in range(1,T+1):
    a=str(raw_input()).split(' ')
    count=0
    string=a[0]
    k=int(a[1])
    st=[]
    for j in string:
        st.append(j)
    for j in range(0,len(st)):
        if st[j]=='-':
            if len(st)-j>=k:
                count+=1
                for l in range(j,j+k):
                    if st[l]=='-':
                        st[l]='+'
                    else:
                        st[l]='-'
                    
        
    flag=0
    for j in st:
        if j=='-':
            flag=1
            break
    if flag==0:
        print "Case #%d: %d"%(i,count)
    else:
        print "Case #%d: IMPOSSIBLE"%i
