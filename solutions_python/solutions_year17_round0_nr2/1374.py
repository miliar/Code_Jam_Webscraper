from functools import reduce

file_in = open('input.in', 'r')
file_out = open('output.out', 'w')

T = int(file_in.readline())


def tidy(n):
    return all([n[i+1] >= n[i] for i in range(len(n) - 1)])

for t, line in enumerate(file_in):

    K = [int(d) for d in line.replace('\n', '')]

    p = len(K) - 1
    while not tidy(K):
        K[p] = 9
        if K[p - 1] > 0:
            K[p - 1] -= 1
        p -= 1
        print(K)

    f = ''
    for d in K:
        f += str(d)

    f = str(int(f))

    file_out.write('Case #{0}: {1}\n'.format(t + 1, f))


file_in.close()
file_out.close()