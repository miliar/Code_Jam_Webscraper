t = int(input())
for i in range(1, t+1):
    n = input()
    for j in range(len(n)-1, 0, -1):
        if int(n[j-1]) > int(n[j]):
            temp = int(n[j-1]) - 1
            n = n[:j-1] + str(temp) + '9'*(len(n)-j)
    print("Case #{}: {}".format(i, int(n)))