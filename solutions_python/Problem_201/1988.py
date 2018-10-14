def calc(arr, K):
    arr1 = [0 for i in range(len(arr) * 2)]
    # print(K, arr)
    for i in range(len(arr)):
        x = arr.index(max(arr))
        arr1[x * 2] = (int((arr[x] - 1) / 2))
        arr1[x * 2 + 1] = ((arr[x] - 1) - int((arr[x] - 1) / 2))
        arr[x] = 0
        K -= 1
        if K == 0:
            return arr1[x * 2], arr1[x * 2 + 1]
    return calc(arr1, K)


def calc_stall(inp):
    N, K = inp.split(' ')
    N, K = int(N), int(K)

    result = calc([N], K)
    return '%s %s' % (max(result), min(result))


if __name__ == '__main__':
    count = int(input())
    for x in range(count):
        inp = input()
        print("Case #%s: %s" % (x + 1, calc_stall(inp)))
