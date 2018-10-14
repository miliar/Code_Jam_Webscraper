in_file = 'C-small-2-attempt0.in'
out_file = 'C-small-2.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    n, k = list(map(int, inp.readline().split()))
    i = 1
    while k > 2**i - 1:
        i += 1
    maximum = (n-k)/(2**i)
    minimum = int(maximum)

    if maximum - int(maximum) >= 0.5:
        maximum = int(maximum) + 1
    else:
        maximum = int(maximum)

    out.write('Case #{}: {} {}\n'.format(case, maximum, minimum))

inp.close()
out.close()
