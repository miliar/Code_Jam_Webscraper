def best(c, f, x):
    p = 2
    farm_penalty = c / p
    build_time = 0
    
    while x / p > farm_penalty + x / (p + f):
        build_time += farm_penalty
        p += f
        farm_penalty = c / p
    
    return build_time + x / p


f = open('/Users/jolleon/Downloads/B-large.in')
for i, l in enumerate(f):
    if i == 0:
        continue
    c, f, x = map(float, l.split())
    print 'Case #%d: %f' % (i, best(c, f, x))
