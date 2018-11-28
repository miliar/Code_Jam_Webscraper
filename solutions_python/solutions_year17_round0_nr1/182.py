input_file = open('A-large.in', 'r')
out_file = open('A-res-large.out', 'w')

test_cases = int(input_file.readline())

for t in range(1, test_cases + 1):
    data = input_file.readline().split(' ')
    s = list(data[0])
    n = len(s)
    k = int(data[1])

    tries = 0
    for i, x in enumerate(s):
        if s[i] == '-' and i + k > n:
            tries = None
            break

        if s[i] == '-':

            tries += 1
            for j in range(k):
                s[i + j] = '+' if (s[i+j] == '-') else '-'
            # print(s, tries)

    print(s, k, tries)
    out_file.write('Case #{:d}: {}\n'.format(t, str(tries) if tries is not None else "IMPOSSIBLE"))
    # print('Case #{:d}: {}\n'.format(t, str(tries) if tries else "IMPOSSIBLE"))

out_file.close()