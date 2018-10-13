def magic(arr1, arr2):
    row1=set(arr1)
    row2=set(arr2)
    commonElem=row1.intersection(row2)
    if len(commonElem)==1:
        for i in commonElem:
            return i
    elif len(commonElem)>1:
        return "Bad magician!"
    return "Volunteer cheated!"

t=int(input())
for i in range(t):
    x=[]
    y=[]
    choice1=int(input())
    for j in range(4):
        x.append(list(map(int, input().split())))
    choice2=int(input())
    for j in range(4):
        y.append(list(map(int, input().split())))
    ans=magic(x[choice1-1], y[choice2-1])
    print('Case #{0}: {1}'.format(i+1, ans))

    