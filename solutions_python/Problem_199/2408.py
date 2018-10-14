tcs = int(input())
for tc in range(1, tcs+1):
    s, p = input().split()
    s = list(s)
    k = int(p)
    counter = 0
    for i in range(len(s)-k+1):
        if s[i] == "+":
            continue
        for f in range(k):
            if s[i+f] == "+":
                s[i+f] = "-"
            else:
                s[i+f] = "+"
        counter += 1
    possible = True
    for i in range(len(s)):
        if s[i] == "-":
            possible = False
            break
    print("Case #", tc, ": ", counter if possible else "IMPOSSIBLE", sep="")
