from collections import defaultdict

input_file = 'C-large.in'
# input_file = 'b.in'
output_file = 'C.out'



with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for case_nr in xrange(1, cases + 1):
            n, k = map(int, f.readline().split())
            d = defaultdict(int)
            q = [n]
            d[n] = 1
            count = 0
            curr, curr1 = 0, 0
            while q:
                # print 'count, k', count, k
                l = q.pop(0)
                if count >= k:
                    break
                num = d[l]
                count += num
                curr = l / 2
                curr1 = (l-1) / 2
                d[curr] += num
                d[curr1] += num
                if curr not in q:
                    q.append(curr)
                if curr1 not in q:
                    q.append(curr1)
                # print '##curr, curr1', curr, curr1
            # print 'n, k', n, k
            # print 'curr, curr1', curr, curr1
            # print q
            ans = ' '.join(map(str, (max(curr, curr1), min(curr, curr1))))

            print 'Case #{i}: {res}'.format(res=ans, i=case_nr)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=case_nr))
