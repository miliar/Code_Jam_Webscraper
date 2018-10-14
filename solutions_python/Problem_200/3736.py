t=int(raw_input(''))
for i in xrange(1,t+1):
   
    num=int(raw_input(''))
    le=len(str(num))
    l=len(str(num))-1
    sl=len(str(num))-2
    
    dig=[]
    dig1=[]
    lu=[]
    str1=''
    list1=[]
    dig = list(int(d) for d in str(num))
    for s in xrange(len(dig)):
        list1.append(dig[s])
    for s in xrange(len(dig)-1):
        if dig[sl]>dig[l]:
            dig[sl]=dig[sl]-1
            dig[l]=9
            for o in xrange(l+1,le):
                dig[o]=9
            sl=sl-1
            l=l-1
        else:
            sl=sl-1
            l=l-1
    dig1 = list(str(d) for d in dig)


    s=''
    
    
    str1 = ''.join(dig1)
    s = str(int(str1))
    print "Case #"+str(i)+":",s
