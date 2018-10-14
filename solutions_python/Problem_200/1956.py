def validate(n):
    lst = list(map(int, str(n)))
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def determine_1(n):
    i = n
    while True:
        if validate(i):
            return i
        else:
            i -= 1


def determine_2(n):
    lst = list(map(int, str(n)))
    buffer = [lst[0]]
    all = []
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            buffer.append(lst[i])
        elif lst[i] != lst[i - 1]:
            all.append([buffer[0], len(buffer)])
            buffer = [lst[i]]
    all.append([buffer[0], len(buffer)])

    is_downgraded = False
    new_all = []
    for i in range(len(all) - 1):
        if not is_downgraded and all[i][0] > all[i + 1][0]:
            new_all.append([all[i][0] - 1, 1])
            new_all.append([9, all[i][1] - 1])
            is_downgraded = True
        elif is_downgraded:
            new_all.append([9, all[i][1]])
        else:
            new_all.append(all[i])

    if not is_downgraded:
        new_all.append(all[len(all) - 1])
    elif is_downgraded:
        new_all.append([9, all[len(all) - 1][1]])

    s = ''
    for lst in new_all:
        s += str(lst[0]) * lst[1]

    return int(s)


T = int(input())

for i in range(T):
    n = int(input())
    print('Case #' + str(i + 1) + ': ' + str(determine_2(n)))

"""
for i in range(1,100001):
    if determine_1(i) != determine_2(i):
        print(i, determine_1(i), determine_2(i))
    else:
        print(i)
"""