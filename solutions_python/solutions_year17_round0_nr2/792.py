
f = open('B-large.in', 'r').readlines()

N = int(f[0])

for t_case in xrange(1, N+1):
    # print('Processing test case #{}'.format(t_case))

    num = ['0'] + list(f[t_case].strip())

    last_strict = 0
    ans = num

    for j in xrange(len(num) - 1):
        # Check next number is ascending
        if num[j+1] < num[j]:
            # Find last strictly increasing number and recreate the string
            ans = num[:last_strict] + [ chr( ord(num[last_strict])-1 ) ] + ['9' * (len(num) - last_strict - 1)]
            break
        elif num[j+1] > num[j]:
            last_strict = j+1

    # Clean up the answer by removing all '0' at the front
    while ans[0] == '0':
        ans = ans[1:]

    print('Case #{}: {}'.format(t_case, ''.join(ans)))

