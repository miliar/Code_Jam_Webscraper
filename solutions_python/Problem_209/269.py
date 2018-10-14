import os
import math

pi = math.acos(-1)

class Solver(object):
    def __init__(self):
        pass
        
    def subsolve(self, cakes, K):
        if K > len(cakes):
            return 0
        subc = cakes[0:-1]
        subc.sort(key=lambda x: x[0]*x[1])
        c = cakes[-1]
        v = c[0]*c[0] + 2*c[0]*c[1]
        for i in range(-1,-K,-1):
            c = subc[i]
            v += 2*c[0]*c[1]
        return pi*v
    
    def solve(self, inputs):
        N, K = [int(x) for x in inputs[0].split()]
        cakes = []
        for i in range(N):
            r, h = [int(x) for x in inputs[i+1].split()]
            cakes.append((r, h))
        cakes.sort(key=lambda x: x[0])
        max_ = 0
        for i in range(K,N+1):
            v = self.subsolve(cakes[:i], K)
            if v > max_:
                max_ = v
        return '%.9f'%max_
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            ns = [int(x) for x in lines[cur].split()]
            case_line_cnt = 1 + ns[0]
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-large.in'
    #iname = 'foo'
    sample_in = '''4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
    '''
    sample_out = '''
Case #1: 138230.076757951
Case #2: 150796.447372310
Case #3: 43982.297150257
Case #4: 625.176938064
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