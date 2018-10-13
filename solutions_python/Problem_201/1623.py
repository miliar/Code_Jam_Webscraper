def put(n, k):

    if n == k:
        return (0, 0)

    # n stalls, k people
    options = {
        n: 1
    }

    best = 0
    while k > 0:
        best = max(options.keys())
        if options[best] > 1:
            options[best] -= 1
        else:
            del options[best]

        if best % 2 == 1:
            last = best // 2
            if last in options:
                options[last] += 2
            else:
                options[last] = 2
        else:
            last = best // 2
            if last in options:
                options[last] += 1
            else:
                options[last] = 1

            if (last - 1) in options:
                options[last - 1] += 1
            else:
                options[last - 1] = 1

        k -= 1

    if best % 2 == 1:
        result = (best // 2, best // 2)
    else:
        result = (best // 2, best // 2 - 1)

    return max(result), min(result)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = input().split(' ')
    print('Case #{}: {}'.format(i, ' '.join(map(str, put(int(n), int(k))))))
