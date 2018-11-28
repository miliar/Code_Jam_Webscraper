n = int(input())

for case in range(1, n + 1):
    s, k = input().split(" ")
    #print(s)
    s = list(s)
    k = int(k)

    n = 0
    for i in range(0, len(s)):
        # print(s)
        if s[i] is '-':
            if i > len(s)-k:
                print("Case #{}: IMPOSSIBLE".format(case))
                break
            else:  # flip it
                n += 1
                for i in range(i+1, i+k):
                    if s[i] is '-':
                        s[i] = '+'
                    else:
                        s[i] = '-'
        else:
            pass
    else:
        print("Case #{}: {}".format(case, n))
