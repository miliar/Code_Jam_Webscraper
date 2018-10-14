t = int(input())
#print (t)
#i=1
n=[]
for i in range(t):
    n.append(int(input()))
for i in range(t):
    temp = n[i]
    while temp>0:
        lst = [int(j) for j in str(temp)]
        lst1=lst
        #print (lst)
        str1 = "".join(str(x) for x in lst1)
        lst.sort()
        str2="".join(str(x) for x in lst)
            #print (lst1)
        if str1==str2:
            break
        else:
            temp=temp-1

    print("Case #"+str(i+1)+": "+str(temp))

