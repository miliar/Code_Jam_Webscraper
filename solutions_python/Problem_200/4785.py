tidy = []

prev = 1
num = 1
for i in range(1, 1001):
    num = int("".join(sorted(str(i))))
    if num == i:
        prev = num
    tidy.append(prev)

t = int(input())
for x in range(t):
    n = int(input())
    print("Case #{}: {}".format(x+1, tidy[n-1]))
    
