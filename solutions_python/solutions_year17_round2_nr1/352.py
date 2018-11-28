f_in = open('A-large.in')
f_out = open('A-large.out', 'w')

T = int(f_in.readline())

def read_ints():
    return [int(x) for x in f_in.readline().rstrip().split()]

def solve():
    D, N = read_ints()
    best_speed = None
    for i in range(N):
        # work out best speed if just riding with this horse
        # ie intersection point at the final destination
        k, s = read_ints()
        speed = (D * s * 1.0) / (D - k)
        # need to take minimum best speed
        if best_speed is None or speed < best_speed:
            best_speed = speed

    return best_speed

for case in range(1, T+1):
    out = 'Case #{}: {}\n'.format(case, solve())
    f_out.write(out)
    print out




f_in.close()
f_out.close()
