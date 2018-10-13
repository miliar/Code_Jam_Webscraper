def inv(S):
    res = ""
    for i in S:
        if i == "-":
            res += "+"
        else:
            res += "-"
    return res

T = int(input())
for j in range(T):
    pan, S= input().split()
    S = int(S)
    out = 0
    for i in range(len(pan) - S + 1):
        if pan[i] == "-":
            pan = pan[:i] + inv(pan[i:i+S]) + pan[i+S:]
            out += 1

    print("Case #{}:".format(j+1), end = " ")
    if "-" in pan:
        print("IMPOSSIBLE")
    else:
        print(out)
