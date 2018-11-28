c = int(raw_input())

for idx in range(c):
    n = list(raw_input())
    l = len(n)

    for _ in range(l):
        prev = n[0]
        for i in range(l):
            if prev > n[i]:
                n[i-1] = str(int(prev) - 1)
                for j in range(i, l):
                    n[j] = '9'
                break
            prev = n[i]
    print "Case #{}: {}".format(idx+1, str(int(''.join(n))))
