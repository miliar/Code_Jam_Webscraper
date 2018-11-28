TestCases = int(input())
for i in range(0,TestCases):
    Number = str(input())
    for j in range(int(Number),int(Number)//2,-1):
        temp1 = str(j)
        for k in range(len(temp1)-1,0,-1):
            if temp1[k] < temp1[k-1]:
                value = False
                break
            else:
                value = True
        if value == True:
            print("Case #{}: {}".format(str(i+1),temp1))
            break