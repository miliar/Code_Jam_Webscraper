def tidy(nl):
    for j in range(len(nl) - 1):
        if nl[j] > nl[j + 1]:
            nl[j] = chr(ord(nl[j]) - 1)
            for k in range(j + 1, len(nl)):
                nl[k] = "9"
            tidy(nl)
    return nl

t = int(input())  
for i in range(1, t + 1):
    n = list(input())
    
    n = tidy(n)

    res = ""
    for ni in n:
        if ni != '0':
            res += ni
    print("Case #{}: {}".format(i, res))
