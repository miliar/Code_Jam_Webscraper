def lister(a):
    b=[]
    for i in str(a):
        b.append(int(i))
    return b

n = int(input())
for i in range(n):
    no = int(input())
    j = int(no)
    while j>0:
        lst = lister(j)
        le = len(lst)
        fl =True
        for  k in range(le-1,0,-1):
            if lst[k]<lst[k-1]:
                if lst[k-1]!=0:
                    lst[k],lst[k-1] = 9,lst[k-1]-1
                    for  f in range(k,le):
                        lst[f] = 9 
                j = int(''.join(str(e)for e in lst ))
        if True:
            print('Case #'+str(i+1)+':',j)
            break
            
        
