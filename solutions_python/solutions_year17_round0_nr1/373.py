import os

class Solver(object):
    def __init__(self):
        pass
    
    def subs(self, s, k):
        r = 0
        i = 0
        while i + k < len(s):
            if s[i] == '+':
                i += 1
                continue
            for j in range(i, i + k):
                if s[j] == '+':
                    break
            r += 1
            t = j
            for j in range(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'
            i = t

        last = s[-1]
        for i in range(k):
            if s[-1-i] != last:
                return -1
        if last == '-':
            return r + 1
        return r
    
    def solve(self, inputs):
        s, k = inputs[0].split()
        k = int(k)
        s = list(s)
        r = self.subs(s, k)
        if r == -1:
            return 'IMPOSSIBLE'
        else:
            return r
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
    iname = 'A-large.in'
    # iname = 'foo'
    sample_in = '''3
---+-++- 3
+++++ 4
-+-+- 4
    '''
    sample_out = '''
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
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