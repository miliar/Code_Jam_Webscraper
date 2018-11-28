'''
IN:

4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21

OUT:

Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3

'''

base_name = 'B_large'
in_name = '{0}.in'.format(base_name)
out_name = '{0}.out'.format(base_name)

in_file = open(in_name)

test_count = int(in_file.readline())

lines = in_file.readlines()
split_lines = (line.strip().split(' ') for line in lines)
inputs = [(int(c[0]), int(c[1]), int(c[2]), [int(n) for n in c[3:]]) for c in split_lines]

for n,s,p,t in inputs:
    assert n == len(t)

def best(ti):
    if ti == 0:
        return 0,0
    if ti == 30:
        return 10,10
    if ti == 29:
        return 10,10

    n = ti // 3
    r = ti % 3

    if r == 0:
        return n,n+1
    if r == 1:
        return n+1,n+1
    if r == 2:
        return n+1,n+2

    raise Exception

global best_dict
best_dict = dict((i, best(i)) for i in range(31))

def solve(s, p, t):
    results = [best_dict[ti] for ti in t]

    guaranteed = sum(1 for a,b in results if a >= p)
    possible = sum(1 for a,b in results if b == p and a < b)

    return guaranteed + min(s, possible)

out_file = open(out_name, 'w')

for i, (n,s,p,t) in enumerate(inputs, 1):
    print('Case #{0}: {1}'.format(i, solve(s,p,t)))
    out_file.write('Case #{0}: {1}\n'.format(i, solve(s,p,t)))

out_file.close()