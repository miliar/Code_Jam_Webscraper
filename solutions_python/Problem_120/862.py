from numpy import poly1d, roots, pi

# 1cm annulus is 2pi r + pi, where r is inner radius

for case in range(1,input()+1):
    R, P = map(float, raw_input('').split())
    p = poly1d([2., 2*R-1, -P])
    print('Case #{0}: {1}'.format(case, int(max(roots(p)))))
