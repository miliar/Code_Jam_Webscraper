n = int(input())
f1 = open("output.txt", 'w', encoding="utf-8")
for i in range(n):
    s = input().split(' ')
    x = list(s[0])
    k = int(s[1])
    if '-' not in x:
        f1.write("Case #" + str(i + 1) + ": 0\n")
    else:
        c = 0
        while True:
            if '-' not in x:
                f1.write("Case #" + str(i + 1) + ": " + str(c) + '\n')
                break
            else:
                j = x.index('-')
                if len(x[j:]) >= k:
                    for z in range(k):
                        if x[j + z] == '-':
                            x[j + z] = '+'
                        else:
                            x[j + z] = '-'
                else:
                    f1.write("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
                    break
                c += 1
