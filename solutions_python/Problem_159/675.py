with open('A-large.in') as f:
    with open('a.out', 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            line = f.readline()
            line = f.readline()
            in_data = line.split(' ')
            mush = map(int, in_data)
            deltas = [mush[j-1] - mush[j] for j in xrange(1, len(mush))]
            y = sum(filter(lambda x: x > 0, deltas))
            mmax = max(deltas)
            z = 0
            for j in mush[:-1]:
                z += min(j, mmax)
            print 'Case #{i}: {y} {z}'.format(y=y, z=z, i=i)
            out.write('Case #{i}: {y} {z}\n'.format(y=y, z=z, i=i))