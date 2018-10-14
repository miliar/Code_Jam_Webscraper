t = int(input())

for task in range(t):
    n = int(input())
    s = str(n)
    e = False
    out = ""
    for i in range(len(s)):
        if not e:
            if int(s[i] * (len(s) - i)) <= int(s[i:]):
                out += s[i]
            else:
                out += str(int(s[i]) - 1)
                e = True
        else:
            out += "9"
    print("Case #{}: {}".format(task+1, int(out)))
