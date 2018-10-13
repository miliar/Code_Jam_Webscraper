import solver

# f_name = 'sample.in'
# f_name = 'A-small-attempt0.in'
f_name = 'A-large.in'

f_out_name = f_name[:-2] + 'out'

with open(f_name) as f_in, open(f_out_name, 'w') as f_out:
    T = int(f_in.readline())
    for i in xrange(T):
        test = solver.parse_input(f_in.readline())
        out = solver.solve(test)
        f_out.write('Case #{0}: {1}\n'.format(i+1, out))


