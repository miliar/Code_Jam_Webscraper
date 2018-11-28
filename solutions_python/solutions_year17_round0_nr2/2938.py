with open('B-large.in', 'r') as f:
    inputs = [int(line) for line in f][1:]


def largest_tidy(N):
    s = str(N)
    original_len = len(s)
    for i in reversed(range(1, original_len)):
        if int(s[i]) < int(s[i - 1]) or int(s[i]) == 0:
            N -= (int(s[i]) + 1) * 10**(len(s) - 1 - i)
            s = str(N)

            if len(s) < original_len:
                original_len = len(s)
                i -= 1

            for j in range(i, len(s)):
                s = list(s)
                s[j] = '9'
                s = ''.join(s)

    return int(s)


with open('out.txt', 'w') as f:
    for i, N in enumerate(inputs):
        output = 'Case #{}: {}\n'.format(i + 1, str(largest_tidy(N)))
        f.write(output)
