def testcase():
    [n, k] = [int(x) for x in input().split(" ")]

    data = {}
    data[n] = 1

    while k > 0:
        mk = max(data.keys())
        count = min(data[mk], k)
        k -= count
        del data[mk]

        left = (mk-1) // 2
        right = mk - 1 - left

        for ns in [left, right]:
            if ns in data:
                data[ns] += count
            else:
                data[ns] = count

    return "{} {}".format(max(left, right), min(left, right))


t = int(input())

for num in range(t):
    print("Case #{num}: {result}".format(num=num+1, result=testcase()))