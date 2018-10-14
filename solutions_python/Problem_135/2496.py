def magic(ans1,arr1,ans2,arr2):
    count=0
    r1=list()
    r2=list()
    for i in range(4):
        r1.append(arr1[ans1-1][i] )
    for i in range(4):
        r2.append(arr2[ans2-1][i])
    for i in range(4):
        for j in range(4):
            if r1[i]==r2[j]:
                count+=1
                ans=r1[i]
    if count == 1:
        return str(ans)
    if count == 0:
        return str("Volunteer cheated!")
    if count >1:
        return str("Bad magician!")

out_file=open('out','w')
in_file=open('in','r')
case=in_file.readline()
for i in range(int(case)):
    ans1=int(in_file.readline())
    arr1=[[],[],[],[]]
    for j in range(4):
        temp1=in_file.readline()
        temp1=temp1.split()
        for k in range(4):
            arr1[j].append(int(temp1[k]))
    ans2=int(in_file.readline())
    arr2=[[],[],[],[]]
    for j in range(4):
        temp2=in_file.readline()
        temp2=temp2.split()
        for k in range(4):
            arr2[j].append(int(temp2[k]))
    sol=magic(ans1,arr1,ans2,arr2)
    out_file.write("Case #{0}: {1}".format((i+1),sol))
    out_file.write("\n")
in_file.close()
out_file.close()
