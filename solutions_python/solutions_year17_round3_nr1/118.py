import math

in_file = 'A-small-attempt0.in'
out_file = 'A-small.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    n, k = list(map(int, inp.readline().split()))

    radii = []
    sa = []
    for i in range(n):
        r, h = list(map(int, inp.readline().split()))
        radii.append(r)
        sa.append(2*math.pi*r*h)

    max_area = 0
    for i in range(n):
        radius = radii[i]
        l = []
        for j in range(n):
            if radii[j] <= radius and j != i:
                l.append(sa[j])
        l.sort(reverse=True)
        area = math.pi*radius**2 + sa[i] + sum(l[:k-1])
        max_area = max(area, max_area)

    out.write('Case #{}: {}\n'.format(case, max_area))

inp.close()
out.close()
