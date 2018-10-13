
mult = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
        'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}


def get_mult(a, b):
    minus = 0
    if a[0] == '-':
        a = a[1]
        minus += 1
    if b[0] == '-':
        b = b[1]
        minus += 1

    res = mult[a][b]

    if res[0] == '-':
        minus += 1
        res = res[1]

    if minus % 2 == 1:
        return '-' + res
    else:
        return res


reverse = {'1': '1', 'i': '-i', 'j': '-j', 'k': '-k'}


def get_reverse(a):
    minus = 0

    if a[0] == '-':
        a = a[1]
        minus += 1

    res = reverse[a]

    if res[0] == '-':
        res = res[1]
        minus += 1

    if minus % 2 == 1:
        return '-' + res
    else:
        return res


T = int(input())
for iter_num in range(1, T + 1):
    l, x = map(int, input().split())

    string = input() * x
    prefix = [string[0]]

    for char in string[1:]:
        prefix.append(get_mult(prefix[-1], char))

    result = False
    for i in range(len(prefix)):
        if prefix[i] == 'i':
            for j in range(i + 1, len(prefix)):
                if get_mult('-i', prefix[j]) == 'j':
                    if get_mult('-k', prefix[-1]) == 'k':
                        result = True
                        break
        if result:
            break

    print("Case #" + str(iter_num) + ": " + ("YES" if result else "NO"))
