def f(l, n, caseno):
    count = 0
    for i in range(len(l)-n+1):
    	if l[i] == "-":
            for j in range(i,i+n):
                if l[j] == "-": l[j] = "+"
                elif l[j] == "+": l[j] = "-"
            count += 1
    if l[i:] == ["-"]*n:
        count += 1
        print("Case #%d: %d" %(caseno,count))
    elif l[i:] != n*["+"]:
        count = -1
    return count

x = int(input())
l = []
for i in range(x):
    l.append(input().split(" "))
for i in range(x):
    n = f(list(l[i][0]), int(l[i][1]), i+1)
    if n == -1:
    	print("Case #%d: IMPOSSIBLE" %(i+1))
    else:
	    print("Case #%d: %d" %(i+1,n))
    
