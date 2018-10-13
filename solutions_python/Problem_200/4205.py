test_case=raw_input('')
test_case=int(test_case)

for k in range(1,test_case+1,1):
    st=str(raw_input(''))
    point,check=0,0
    
    l=len(st)
    for j in range(0,l-1,1):
        if st[j]>st[j+1]:
            check=1
            break
    
    if check==0:
        print 'Case #%d: %d'%(k,int(st))
    
    else:
        panga=0
        for j in range(0,l-1,1):
            if st[j]>=st[j+1]:
                point,panga=j,1
                break
        
        if panga==1:
            mpower=pow(10,l-point-1)
            mpower=int(mpower)
            st=int(st)
            st=st-st%mpower
            print 'Case #%d: %d'%(k,st-1)
        else:
            print 'Case #%d: %d'%(k,int(st))