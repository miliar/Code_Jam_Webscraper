for i in range(input()):
    n = list(raw_input())
    j=0
    if len(n)==1:
        print "Case #" + str(i+1) + ": " + str(n[0])
        continue
    flag = False
    while j<len(n)-1:
        if n[j]>n[j+1]:
            flag = True
            break
        j+=1
    if flag==False:
        print "Case #" + str(i+1) + ": " + str(''.join(n))
        continue
    s = '9'*(len(n)-j-1)
    #print j
    n[j]=str(int(n[j])-1)
    k = int(j)
    while j>0:
        if n[j]>=n[j-1]:
            break
        n[j]='9'
        n[j-1] = str(int(n[j-1])-1)
        j-=1
    print "Case #" + str(i+1) + ": " + str(int(''.join(n[:k+1])+s))
    
