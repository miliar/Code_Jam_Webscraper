# Justin Ghan <justin.ghan@gmail.com>

f_name = 'B-large'
f_in = open(f_name + '.in', 'r')
f_out = open(f_name + '.out', 'w')

num_cases = int(f_in.readline().strip())

for idx_case in range(num_cases):
    N, P = [int(s) for s in f_in.readline().strip().split()]
    
    a = 2
    b = 2 ** (N - 1)
    t = b
    p = P
    y = 0
    while True:
        if p <= t:
            break
        y += a
        a *= 2
        b /= 2
        t += b
        if b < 1:
            y = 2 ** N - 1
            break
    
    a = 1
    b = 2 ** (N - 1)
    t = 2 ** N - 1
    p = P
    z = 2 ** N - 1
    while True:
        if p > t:
            break
        z -= a
        a *= 2
        t -= b
        b /= 2
        if b < 1:
            z = 0
            break
    
    f_out.write('Case #{}: {} {}\n'.format(idx_case+1, y, z))

f_in.close()
f_out.close()