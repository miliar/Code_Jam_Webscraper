a=open('A-small-attempt0.txt')
o=open('output2.txt','w')
T=int(a.readline())
for t in range(1,T+1):
    n1=int(a.readline())
    arr1=[]
    for i in range(0,4):
        arr1.append([int(x) for x in a.readline().split()])
    n2=int(a.readline())
    arr2=[]
    for i in range(0,4):
        arr2.append([int(x) for x in a.readline().split()])
    found=0
    ele=0
    for i in arr1[n1-1]:
        for j in arr2[n2-1]:
            if i==j:
                found+=1
                ele=i
                continue
    if found==0:
        o.write("Case #"+`t`+": Volunteer cheated!\n")
    elif found==1:
        o.write("Case #"+`t`+": "+`ele`+"\n")
    else:
        o.write("Case #"+`t`+": Bad magician!\n")
