input_file = open('B-large.in', 'r')
out_file = open('B-res-large.out', 'w')

test_cases = int(input_file.readline())

for t in range(1, test_cases + 1):
    n = input_file.readline().strip()
    s = [int(x) for x in list(n)]
    # print(s)

    must_decrease = False
    for i in range(len(s) - 1, -1, -1):
        if must_decrease:
            if s[i] == 0:
                s[i] = 9
                continue
            else:
                s[i] -= 1
                must_decrease = False
        flag = True
        for j in range(i, 0, -1):
            if s[j-1] > s[j]:
                flag = False
                break

        if flag:
            break

        s[i] = 9
        must_decrease = True

    i = 0
    while s[i] == 0 and i < len(s):
        i += 1
    if i == len(s):
        print("!!!!!!!!!!!!!!!AHTUNG")
    s = s[i:]

    res = "".join([str(x) for x in s])
    out_file.write('Case #{:d}: {}\n'.format(t, res))
    # print('Case #{:d}: {}\n'.format(t, str(tries) if tries else "IMPOSSIBLE"))

out_file.close()