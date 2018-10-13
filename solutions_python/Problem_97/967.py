def combination(word,minval,maxval):
    lst=[word]
    oldval=int(word)        
    lent=len(word)
    count=0
    for i in range(0,lent-1):        
        word=word[-1]+word[0:lent-1]
        newval=int(word)
        if newval>=minval and newval<=maxval and oldval<newval and word not in lst:
            lst.append(word)
            count=count+1            
    return lst,count

f = open('C-small-attempt0.in','r')
arr= f.readlines()
f.close()

f=open('C.out','w')
c=int(arr[0])+1
for case in range(1,c):
    minmax=arr[case].split()
    minval=int(minmax[0])
    maxval=int(minmax[1])
    count=0
    for i in range(minval,maxval+1):
        lst_comb,c=combination(str(i),minval,maxval)        
        count=count+c                            
    f.write("Case #"+str(case)+": "+str(count)+"\n")

f.close()    
