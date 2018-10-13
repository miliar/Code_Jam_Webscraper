t = int(input())

for j in range(t):
    num1 = input()
    snum1=""
    snum = str(num1)
    l1=[]
    l2=[]
    flag=0
    i=len(snum)-1
    
    for k in (snum):
        l1.append(k)
    
    i=0
    
    while(i<len(l1)-1):
        if l1[i]<l1[i+1]:
            i = i + 1
            continue
        if l1[i]==l1[i+1]:
            l2.append(str(int(l1[i])))
            for n in range(i):
                l2.append(l1[n])
            m=i
            flag=2
            while(l1[m]==l1[m+1]):
                l2.append('9')
                m=m + 1
                if m==len(l1)-1:
                    break
            i=m
        else:
            if flag==2:
                l2[n]=str(int(l2[n])-1)
                for l in range(i+1,len(l1)):
                    l2.append(str(9))
                l1=l2
                break
            l1[i]=str(int(l1[i]) - 1)
            for l in range(i+1,len(l1)):
                l1[l] = str(9)
                flag=1
            if flag==1:
                break
    
    for k in (l1):
        if k != '0':
            snum1=snum1+k
    
    str1 = "Case #"+str(j + 1)+": "+snum1
    print(str1)