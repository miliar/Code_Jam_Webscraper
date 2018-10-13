t=int(input())
for t in range(t):
    st=input()
    st=list(st)
    st.reverse()
    #print(st)
    print('Case #',end='')
    print(t+1,end=': ')
    for i in range(len(st)-1):
        if(st[i]>=st[i+1]):
            continue
        else:
            st[i+1]=str(int(st[i+1])-1)
            for j in range(i+1):
                st[j]='9'
        
            
    st.reverse()
    st=''.join(st)
    print(int(st))
            
