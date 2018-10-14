t = int(input())  
for i in range(1, t + 1):
    s, k = input().split(" ")
    s = list(s)
    k = int(k)

    res = 0
    for j in range(len(s) - k + 1):       
        if s[j] == "-":
            res += 1
            #s[j] = "+"
            for l in range(1, k):
                if s[j + l] == "-":
                    s[j + l] = "+"
                else:
                    s[j + l] = "-"
    s = s[len(s) - k + 1:]
    if "-" in s:    
        res = "IMPOSSIBLE"    
    print("Case #{}: {}".format(i, res))
