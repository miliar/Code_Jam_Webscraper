#!/usr/bin/env python

def diff_only_one(r1, r2):
    same = None
    for i in r1:
        if i in r2:
            if same is not None:
                return -1
            else:
                same = i
    return same

def main():
    
    grid = 4
    fh = file('A-small-attempt0.in', 'r')
    t = fh.readline()
    t = t.replace('\n', '')
    t = int(t)
    out = file('A-small-attempt0.out', 'w')

    for case in xrange(0, t):
        ans1 = fh.readline().replace('\n', '')
        
        # print 'ans1: ', ans1
        for g in xrange(0, grid):
            row = fh.readline()
            if g == int(ans1) - 1:
                candidate = row.replace('\n', '').split(' ')
        
        # print candidate
        
        
        ans2 = fh.readline().replace('\n', '')
        # print 'ans2: ', ans2
        
        rows = []
        for g in xrange(0, grid):
            rows.append(fh.readline().replace('\n', '').split(' '))
        same = diff_only_one(candidate, rows[int(ans2) - 1])
        if same is None:
            res = 'Volunteer cheated!'
        elif same < 0:
            res = 'Bad magician!'
        else:
            res = same
            
        print 'Case #%d: %s' % (case+1, res)
        out.write('Case #%d: %s\n' % (case+1, res))


    out.close()
    fh.close()

main()
