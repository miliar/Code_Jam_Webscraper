def calc(N):
    last_num = ''
    digit_count = len(N)
    for j in range(digit_count - 1):
        if int(N[j]) <= int(N[j + 1]):
            last_num += N[j]
        else:
            last_num += str(int(N[j]) - 1) if last_num != '' or int(N[j]) - 1 != 0 else ''
            last_num += (digit_count - j - 1) * '9'
            return calc(last_num)
    else:
        last_num = N
    return last_num


T = int(input().strip())
for i in range(T):
    N = input().strip()
    print("Case #%d: %s" % (i+1, calc(N)))
