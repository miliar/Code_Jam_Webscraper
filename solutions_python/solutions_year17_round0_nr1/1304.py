
file_in = open('input.in', 'r')
file_out = open('output.out', 'w')

T = int(file_in.readline())

for t, line in enumerate(file_in):
    pancakes, K = line.split()
    pancakes = [True if n == '+' else False for n in pancakes]
    K = int(K)

    def flip(p):
        for i in range(p, p + K):
            pancakes[i] = not pancakes[i]

    times = 0
    for i in range(len(pancakes) - K + 1):
        if not pancakes[i]:
            flip(i)
            times += 1

    file_out.write('Case #{0}: {1}\n'.format(t + 1, times if all(pancakes) else 'IMPOSSIBLE'))


file_in.close()
file_out.close()