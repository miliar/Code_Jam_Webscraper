def tidy(num):
    if len(num) == 1:
        return num
    arr = list(map(int, list(num)))
    l = len(arr)
    flag = 0
    for i in range(l - 1):
        if flag == 1:
            arr[i] = 9
        if arr[i] > arr[i + 1] and flag == 0:
            flag = 1
            if i > 0:
                j = i - 1
                while arr[j] == arr[j + 1]:
                    arr[j + 1] = 9
                    j -= 1
                arr[j + 1] -= 1
            else:
                arr[i] -= 1

    if flag:
        arr[-1] = 9
        if arr[0] == 0:
            arr.pop(0)
    return ''.join(list(map(str, arr)))


for i in range(int(input().strip())):
    print("Case #%d: %s" % (i + 1, tidy(input().strip())))
