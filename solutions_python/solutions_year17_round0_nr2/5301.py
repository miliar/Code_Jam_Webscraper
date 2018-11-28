x=int(input())
cases=[]


for i in range(x):
    y= str(input())
    cases.append(y)

for j in range(0,x):
    for p in range(int(cases[j]),0,-1):
        flag = True
        for k in range(len(str(p))-1):
            if int(str(p)[k])> int(str(p)[k+1]):
                flag = False
                break
        if flag== True:
            print("case #"+str(j+1)+":",p)
            break
