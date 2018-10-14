def is_tidy(number):
    a = number
    b = list(number)
    b.sort()
    return a == "".join(b)


ncase = int(raw_input())
for case in range(ncase):
    ori_n = raw_input()
    n = list(ori_n)
    while(True):
        n_str = "".join(n)
        if is_tidy(n_str):
            if int(n_str) > int(ori_n):
                n.pop(0)
                n_str = "".join(n)
            last_tidy = str(int(n_str))
            break
        for i in range(len(n) - 1, -1, -1):
            if i == len(n) - 1:
                prev = n[i]
                continue
            curr = n[i]
            if int(prev) < int(curr):
                for j in range(i + 1, len(n)):
                    n[j] = '9'
                if (n[i] == '0'):
                    n[i] == '9'
                    if i > 0:
                        n[i - 1] = str(int(n[i - 1]) - 1)
                else:
                    n[i] = str(int(n[i]) - 1)
                break
            prev = n[i]

    print "Case #{}: {}".format(case + 1, last_tidy)
