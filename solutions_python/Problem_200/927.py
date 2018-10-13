def dec_num(s, i):
    while i >= 0:
        if s[i] == 0:
            i -= 1
        else:
            s[i] -= 1
            break
    s[i+1:] = [9] * (len(s) - (i+1))

    while len(s) != 0 and s[0] == 0:
        del s[0]


def requires_raise(s):
    r = (len(s) + 1) // 2
    return any(s[i] > s[-(1 + i)] for i in range(r))


def drop_num(s):
    r = (len(s) + 1) // 2
    for i in range(r):
        s[-(1 + i)] = s[i]


def raise_num(s):
    if len(s) % 2 == 0:
        i = len(s) // 2
        if s[i] > s[i - 1]:
            s[i] = s[i - 1]
        else:
            dec_num(s, i - 1)
    else:
        i = len(s) // 2
        dec_num(s, i)


t = int(input())

for case in range(t):
    num_array = [int(x) for x in input().strip()]

    done = False
    while not done:
        done = True
        for i in range(len(num_array)-1):
            if num_array[i] > num_array[i+1]:
                dec_num(num_array, i)
                done = False
                break

    print("Case #{0}: {1}".format(case+1, ''.join(map(str, num_array))))
