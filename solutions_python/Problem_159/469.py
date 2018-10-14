import os

class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        cc = [int(x) for x in inputs[1].split()]
        y = 0
        for i in range(1, len(cc)):
            if cc[i] < cc[i-1]:
                y += cc[i-1] - cc[i]
        
        tx = 0
        for i in range(1, len(cc)):
            if tx < cc[i-1] - cc[i]:
                tx = cc[i-1] - cc[i]
        z = 0
        for i in range(len(cc) - 1):
            if cc[i] > tx:
                z += tx
            else:
                z += cc[i]
        
        return '%d %d'%(y, z)
            
        
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            case_line_cnt = 2
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-large.in'
#     iname = 'foo'
    sample_in = '''
4
4
10 5 15 5
2
100 100
8
81 81 81 81 81 81 81 0
6
23 90 40 0 100 9
    '''
    sample_out = '''
Case #1: 15 25
Case #2: 0 0
Case #3: 81 567
Case #4: 181 244
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