n=int(input())
a=[]
for i in range(n):
    s=input().strip()
    a.append(s)
for i in range(n):
    for j in range(int(a[i])):
        if(len(a[i])==3):
            if(int(a[i][2])>=int(a[i][1])>=int(a[i][0])):
                print("Case #"+str(i+1)+": "+str(a[i]))
                break
            else:
                a[i]=str(int(a[i])-1)
        elif(len(a[i])==2):
            if(int(a[i][1])>=int(a[i][0])):
                print("Case #"+str(i+1)+": "+str(a[i]))
                break
            else:
                a[i]=str(int(a[i])-1)
        elif(len(a[i])==1):
            print("Case #"+str(i+1)+": "+str(a[i]))
            break;
        elif(a[i]=="1000"):
            print("Case #"+str(i+1)+": "+str(999))
            break
        
