import math
file_in = open('input.in', 'r')
file_out = open('output.out', 'w')

T = int(file_in.readline())

def foo(K):
    return (K // 2, K // 2 - 1) if K % 2 == 0 else (K // 2, K // 2)


for t, line in enumerate(file_in):
    N, K = int(line.split()[0]), int(line.split()[-1])
    while K > 1:
        K -= 1
        N = max(foo(N)) if K % 2 != 0 else min(foo(N))
        K = math.ceil(K / 2)
    s_max, s_min = foo(N)
    file_out.write('Case #{0}: {1} {2}\n'.format(t + 1, s_max, s_min))


file_in.close()
file_out.close()