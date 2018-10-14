def check(n):
    l = []
    while(n > 0):
        l.append(int(n%10))
        n = int(n/10)
    for k in range(len(l) - 1):
        if(l[k] < l[k+1]):
            return 0
    return 1


last = 1
x = input()
for i in range(int(x)):
    y = input()
    for j in range(1,int(y) + 1): 
        if(check(j) == 1):
            last = j
    print("Case #" + str(i+1) + ": " + str(last))