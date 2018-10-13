def lot(A,B,K):
    z=[]
    for i in range(A):
        for j in range(B):
            z.append((i,j))
    count=0
    for i in z:
        #l=int(bin(i[0])[2:]) & int(bin(i[1])[2:])
        #l=int(str(l),2)
        if(K>(i[0]&i[1])):
            count+=1
    return count

with open("data.txt") as f:
    content = f.readlines()
cases=int(content[0])
content=content[1:]
for i in range(cases):
    case=content[i]
    case1=case.split(" ")
    A=int(case1[0])
    B=int(case1[1])
    C=int(case1[2])
    sol=lot(A,B,C)
    print "Case #" + str(i+1) + ": " + str(sol)
