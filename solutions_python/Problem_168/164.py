import os

d_up = '^'
d_down = 'v'
d_left = '<'
d_right = '>'
d_no = '.'
        
class Solver(object):
    def __init__(self):
        pass
    
    def fd(self, mtx, arrow):
        rr = len(mtx)
        cc = len(mtx[0])
        tr, tc, d = arrow
        if d == d_up:
            for r in range(tr-1, -1, -1):
                if mtx[r][tc] != d_no:
                    return r, tc, mtx[r][tc]
        elif d == d_down:
            for r in range(tr+1, rr):
                if mtx[r][tc] != d_no:
                    return r, tc, mtx[r][tc]
        elif d == d_left:
            for c in range(tc-1, -1, -1):
                if mtx[tr][c] != d_no:
                    return tr, c, mtx[tr][c]
        elif d == d_right:
            for c in range(tc+1, cc):
                if mtx[tr][c] != d_no:
                    return tr, c, mtx[tr][c]
    
    def solve(self, inputs):
        rr, cc = [int(x) for x in inputs[0].split()]
        mtx = []
        for line in inputs[1:]:
            line.strip()
            mtx.append(list(line))
        arr = []
        for tr in range(rr):
            for tc in range(cc):
                if mtx[tr][tc] != d_no:
                    arr.append((tr, tc, mtx[tr][tc]))
        cnt = 0
        for a in arr:
            next = self.fd(mtx, a)
            if next:
                continue
            found = False
            a_up = (a[0], a[1], d_up)
            a_down = (a[0], a[1], d_down)
            a_left = (a[0], a[1], d_left)
            a_right = (a[0], a[1], d_right)
            if a_up != a and not found:
                if self.fd(mtx, a_up):
                    found = True
            if a_down != a and not found:
                if self.fd(mtx, a_down):
                    found = True
            if a_left != a and not found:
                if self.fd(mtx, a_left):
                    found = True
            if a_right != a and not found:
                if self.fd(mtx, a_right):
                    found = True
            if not found:
                return 'IMPOSSIBLE'
            else:
                cnt += 1
        return cnt
            
        
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            r = int(lines[cur].split()[0])
            case_line_cnt = 1 + r
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-large.in'
#     iname = 'foo'
    sample_in = '''
4
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.
    '''
    sample_out = '''
Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 0
    '''
    if os.path.exists(iname):
        with open(iname) as f:
            inputs = f.readlines()
    else:
        inputs = [x.strip() for x in sample_in.split('\n') if x.strip()]
    solver = Solver()
    outputs = solver.feed(inputs)
    fail_flag = False
    if os.path.exists(iname):
        with open(iname+'.out', 'w') as f:
            for i, v in enumerate(outputs):
                print >> f, 'Case #%d: %s'%(i+1, str(v))
    else:
        ans = set([x.strip() for x in sample_out.split('\n') if x.strip()])
        for i, v in enumerate(outputs):
            t = 'Case #%d: %s'%(i+1, str(v))
            if t not in ans:
                print '!!! Wrong:', t
                fail_flag = True
    print '===================================================='
    for i, v in enumerate(outputs):
        print 'Case #%d: %s'%(i+1, str(v))
    print '===================================================='
    print 'done' if not fail_flag else 'fail'
    pass