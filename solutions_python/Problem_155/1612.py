test = int(input())

answer = []
for x in range(test):
    shy = input().strip().split()
    shym = int(shy[0])
    shylist = list(shy[1])
    shylist = [int(x) for x in shylist]
    ans = ""
    needed = 0
    y = 0
    for i in range(len(shylist)):
        if needed < i:
            y += i-needed
            needed += (i-needed)
        needed += shylist[i]
        
    ans = "Case #" + str(x+1) + ": " + str(y)
    answer.append(ans)

for i in answer:
    print(i)
