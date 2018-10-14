input_file = 'A-large.in'
output_file = 'A.out'

flip = {'-':'+', '+':'-'}

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = int(f.readline())
        for i in xrange(1, cases+1):
            line = f.readline()
            pancakes, n = line.split()
            n = int(n)
            queue = []
            nn = 0
            for p in pancakes:
                queue.append(p)
                # print queue
                if len(queue) == n:
                    if queue[0] == '-':
                        nn += 1
                        for j in range(1, len(queue)):
                            queue[j] = flip[queue[j]]
                    queue.pop(0)
            # print queue, '-' in queue
            if '-' in queue:
                ans = 'IMPOSSIBLE'
            else:
                ans = nn
            print 'Case #{i}: {res}'.format(res=ans, i=i)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=i))
