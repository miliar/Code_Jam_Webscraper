#!/usr/bin/env python2.6

#in_file = 'A-test.in'
#out_file = 'A-test.out'
#in_file = 'A-small-attempt0.in'
#out_file = 'A-small.out'
in_file = 'A-large.in'
out_file = 'A-large.out'

with open(in_file) as input:
    with open(out_file, 'w') as output:
        T = int(input.readline().rstrip())
        for t in range(1,T+1):
            N, M = input.readline().rstrip().split(None, 1)
            existing = set()
            for n in range(0, int(N)):
                existing.add(input.readline().rstrip())
            desired = []
            for m in range(0,int(M)):
                desired.append(input.readline().rstrip())

            count_mkdir = 0
            for dir in desired:
                dir_parts = dir.split('/')[1:]
                for i in range(1, len(dir_parts)+1):
                    s_dir = '/' + '/'.join(dir_parts[0:i])
                    if s_dir not in existing:
                        count_mkdir = count_mkdir + 1
                        existing.add(s_dir)



            print >> output, 'Case #%d: %s' % (t,count_mkdir)