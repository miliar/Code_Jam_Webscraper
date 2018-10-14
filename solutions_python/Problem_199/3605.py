def func(a,b):
    list1 = list(a)
    val = len(list1)
    counter = 0
    for x in range(val-b+1):
        if list1[x]=="-":
            for y in range(b):
                if list1[x+y]=="-":
                    list1[x+y] = "+"
                else:
                    list1[x+y]="-"
            counter = counter+1
    if "-" in list1:
        counter = "IMPOSSIBLE"
    return counter
n = int(input())
list2 = []
for m in range(n):
    c,d = input().split(" ")
    d = int(d)
    val = func(c,d)
    list2.append(val)
for z in range(n):
    print("Case #"+str(z+1)+": "+str(list2[z]))
    
