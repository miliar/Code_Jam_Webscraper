import os
import math

class Solver(object):
    def __init__(self):
        pass
    
    def dump(self, cc, rslt):
        if cc in self.dd:
            co = self.dd.pop(cc)
            for i in range(co[1]):
                self.dump(cc, rslt)
                self.dump(co[0], rslt)
        rslt.append(cc)
    
    def solve(self, inputs):
        N, R, O, Y, G, B, V = [int(x) for x in inputs[0].split()]
        self.dd = {'R':('G', G), 'Y':('V', V), 'B':('O', O)}
        rslt = []
        rr = R - G
        yy = Y - V
        bb = B - O
        #print rr, yy, bb
        if (rr < 0) or (yy < 0) or (bb < 0):
            return 'IMPOSSIBLE'
        if (rr == 0) and (G != 0):
            if (any([O, Y, B, V])):
                return 'IMPOSSIBLE'
            else:
                self.dump('R', rslt)
                return ''.join(rslt[:-1])
        if (rr == 0) and (V != 0):
            if (any([R, O, G, B])):
                return 'IMPOSSIBLE'
            else:
                self.dump('Y', rslt)
                return ''.join(rslt[:-1])
        if (rr == 0) and (O != 0):
            if (any([R, Y, G, V])):
                return 'IMPOSSIBLE'
            else:
                self.dump('B', rslt)
                return ''.join(rslt[:-1])
        cad = [(rr, 'R'), (yy, 'Y'), (bb, 'B')]
        cad.sort(key=lambda x: x[0])
        if cad[0][0] + cad[1][0] < cad[2][0]:
            return 'IMPOSSIBLE'
        a = cad[0][0]
        b = cad[2][0] - a
        c = cad[1][0] - b
        for i in range(b):
            self.dump(cad[2][1], rslt)
            self.dump(cad[1][1], rslt)
        for i in range(c):
            self.dump(cad[2][1], rslt)
            self.dump(cad[1][1], rslt)
            self.dump(cad[0][1], rslt)
        for i in range(a-c):
            self.dump(cad[2][1], rslt)
            self.dump(cad[0][1], rslt)
        return ''.join(rslt)
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            ns = [int(x) for x in lines[cur].split()]
            case_line_cnt = 1
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'B-small-attempt0.in'
    sample_in = '''4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
    '''
    sample_out = '''
Case #1: RYBRBY
Case #2: IMPOSSIBLE
Case #3: YBRGRB
Case #4: YVYV
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