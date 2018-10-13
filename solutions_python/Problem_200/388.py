import os
import math

class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        n = int(inputs[0].strip())
        nn = list(str(n))
        if len(nn) == 1:
            return n
        pre = 0
        for i in range(1, len(nn)):
            if int(nn[i]) > int(nn[i-1]):
                pre = i
            if int(nn[i]) < int(nn[i-1]):
                nn[pre] = str(int(nn[pre])-1)
                for j in range(pre+1, len(nn)):
                    nn[j] = '9'
                break
        
        return int(''.join(nn))
        
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            case_line_cnt = 1
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'B-large.in'
    sample_in = '''4
132
1000
7
111111111111111110
    '''
    sample_out = '''
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
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