import os
import itertools

class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        N, K = [int(x) for x in inputs[0].split()]
        U = [float(x) for x in inputs[1].split()][0]
        P = [float(x) for x in inputs[2].split()]
        P.sort()
        P.append(1.0)
        
        ru = U
        d = 1
        while ru > 0 and d > 0:
            I = N
            d = 0.0
            for i in range(1, len(P)):
                if P[i] > P[i-1]:
                    I = i
                    d = P[i] - P[i-1]
                    break
            if ru > d * I:
                du = d
            else:
                du = ru / I
            for i in range(I):
                P[i] += du
            ru -= du * I
            
        fp = reduce(lambda x,y: x*y, P)
        return '%.6f'%fp
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            ns = [int(x) for x in lines[cur].split()]
            case_line_cnt = 3
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'C-small-1-attempt0.in'
    sample_in = '''4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
2 1
0.0000
0.9000 0.8000
2 1
0.1000
0.4000 0.5000
    '''
    sample_out = '''
Case #1: 1.000000
Case #2: 0.250000
Case #3: 0.980000
Case #4: 0.760000
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