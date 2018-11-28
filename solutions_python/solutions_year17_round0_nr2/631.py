s = str(raw_input(""))
t = int(s)
for case in range(t):
    s = str(raw_input(""))
    a = list(s)
    a = [int(x) for x in a]
    i = 0
    while i < len(a)-1:
        if a[i] <= a[i+1]:
            i += 1
            continue

        if a[i] == 1:
            if i == 0:
                a = [9]*(len(a) - 1)
            else:
                a[i] = 0
                a = a[:i+1] + [9]*(len(a) - i - 1)
                i -= 1
        else:
            a[i] -= 1
            a = a[:i+1] + [9]*(len(a) - i - 1)
            if i>0: i -= 1
    ans = ''.join([str(x) for x in a])
    print("Case #%d: %s" % (case+1, ans))
