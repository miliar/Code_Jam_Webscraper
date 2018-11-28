input_file = open('C-large.in', 'r')
out_file = open('C-res-large.out', 'w')

test_cases = int(input_file.readline())


def f(n, k):
    n -= 1
    if k == 1:
        return (n + 1) // 2, (n // 2)

    k -= 1
    if n % 2 == 0:
        return f(n // 2, (k + 1) // 2)

    if k % 2 == 0:
        return f(n // 2, k // 2)

    return f((n + 1) // 2, (k + 1) // 2)

for t in range(1, test_cases + 1):
    s = input_file.readline().strip()
    n, k = [int(x) for x in s.split(' ')]

    res = f(n, k)
    # print(n, k, res)
    out_file.write('Case #{:d}: {:d} {:d}\n'.format(t, res[0], res[1]))
    # print('Case #{:d}: {}\n'.format(t, str(tries) if tries else "IMPOSSIBLE"))

out_file.close()