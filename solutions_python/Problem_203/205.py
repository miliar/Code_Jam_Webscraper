input_file = 'A-large.in'
output_file = 'A.out'

flip = {'-':'+', '+':'-'}

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            n, k = map(int, f.readline().split())
            grid = [list(f.readline().strip()) for j in range(n)]

            for g, line in enumerate(grid):
                curr = None
                for gg, l in enumerate(line):
                    if l != '?':
                        curr = l
                    elif curr:
                        grid[g][gg] = curr
                for gg, l in list(enumerate(line))[::-1]:
                    if l != '?':
                        curr = l
                    elif curr:
                        grid[g][gg] = curr
            for g, line in enumerate(grid):
                if line[0] == '?' and g > 0:
                    grid[g] = grid[g-1]
            for g, line in list(enumerate(grid))[::-1]:
                if line[0] == '?':
                    grid[g] = grid[g+1]

            ans = '\n'.join([''] + map(''.join, grid))
            print 'Case #{i}: {y}'.format(y=ans, i=i)
            out.write('Case #{i}: {y}\n'.format(y=ans, i=i))