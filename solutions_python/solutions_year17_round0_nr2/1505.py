t = int(input())
for r in range(t):
    n = str(input())
    ans = list(n)


    for index in range(len(n)-1,-1,-1):

        if index == 0:
            break
        if ans[index] < ans[index-1]:
            for i2 in range(index,len(n)):
                ans[i2] = "9"
            ans[index-1] = str(int(ans[index-1]) - 1)



    print("Case #%s: %s" % (r + 1, "".join(ans).strip("0")))