test = int(input())

answer = []
for x in range(test):
    shy = input().strip().split()
    shym = int(shy[0])
    shyL = list(shy[1])
    shyL = [int(x) for x in shyL]
    ans = ""
    nd = 0
    y = 0
    for i in range(len(shyL)):
        if nd < i:
            y += i-nd
            nd += (i-nd)
        nd += shyL[i]
        
    ans = "Case #" + str(x+1) + ": " + str(y)
    answer.append(ans)

for i in answer:
    print(i)
