
res_str = 'Case #{0}: {1}'

test_cases = int(input())

for t in range(1, test_cases+1):
    n = int(input())
    n_length = len(str(n))-1
    i = n_length
    while i > 0:
        if int(n / pow(10,i) % 10) > int(n / pow(10,i-1) % 10):
            n = n - ((n % pow(10,i)) + 1)
            i = n_length
        else:
            i -= 1
    print(res_str.format(t, n))
