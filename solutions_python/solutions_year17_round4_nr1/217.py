from collections import Counter

input_file = 'A-small-attempt0.in'
output_file = 'A.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = int(f.readline())
        for i in xrange(1, cases+1):
            n, p = map(int, f.readline().split())
            gg = map(int, f.readline().split())
            groups = Counter([g % p for g in gg])
            ans = -1
            if p == 2:
                ans = groups[0] + (groups[1]+1)/2
            elif p == 3:
                t = min(groups[1], groups[2])
                tt = abs(groups[1] - groups[2])
                ans = groups[0] + t + (tt + 2)/3
            else: # p = 4
                pass

            res = ans
            print 'Case #{i}: {y}'.format(y=res, i=i)
            out.write('Case #{i}: {y}\n'.format(y=res, i=i))