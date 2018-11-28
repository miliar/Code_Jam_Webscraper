#Problem C Recycled Numbers

filename = open("C-small-attempt0.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
filename.close()

testCases = s[0]
newFile = open("output.in","w")

possible=[]
#n = range(s,e+1)
index = 1
caseNumber=1
for i in s[1:]:
    newFile.writelines("Case #%s: "%(caseNumber),)
    caseNumber+=1
    possible=[]
    i=i.split()
    a,b = int(i[0]),int(i[1])
    n = range(a,b+1)
    index = 1
    for i in n:
        for j in n[index:]:
            i,j = str(i),str(j)
            if sorted(i)==sorted(j):
                possible.append((i,j))
        index+=1
    counter = 0
    length = len(str(s))
    for i in possible:
        end = 1
        z = i[0][-end]+i[0][:-end]
        while z!=i[0]:
            if z==i[1]:
                counter+=1
                break
            end+=1
            if end>=length:
                break
            z = i[0][-end:]+i[0][:-end]
    newFile.writelines(str(counter))
    newFile.writelines("\n")

newFile.close()

