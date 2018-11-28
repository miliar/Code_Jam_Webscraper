def tidymax(N):
    idx = -1
    arr = list(str(N))
    tmp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < tmp:
            idx = i - 1
            while 0 < idx:
                if arr[idx - 1] < arr[idx]:
                    break
                idx -= 1
            break
        tmp = arr[i]
    if idx != -1:
        arr[idx] = chr(ord(arr[idx]) - 1)
        for i in range(idx + 1, len(arr)):
            arr[i] = '9'
    return int(''.join(arr))

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    ans = tidymax(N)
    print("Case #%d: %d" % (i, ans))
