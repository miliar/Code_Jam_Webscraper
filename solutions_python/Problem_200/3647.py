def is_tidy(number):
    return ''.join(sorted(str(number))) == str(number)

cases = int(input())
for case in range(1, cases+1):
    n = int(input())
    while True:
        if is_tidy(n):
            print('Case #{}: {}'.format(case, n))
            break
        n -= 1
