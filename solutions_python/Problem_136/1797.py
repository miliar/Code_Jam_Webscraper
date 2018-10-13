'''
Created on 2014-04-11

@author: Wei
'''
'''
Created on 2014-04-11

@author: Wei
'''
import os.path
import paths

class CookieClicker:
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
    
    def solve(self):
        time = 0.0
        gain_rate = 2.0
        while True:
            s = self.C / gain_rate
            time += s
            
            ''' if buy a farm now '''
            new_gain_rate = gain_rate + self.F
            s1 = self.X / new_gain_rate
            ''' if not buy a farm and wait till we get enough cookies '''
            s2 = (self.X - self.C) / gain_rate
            
            if s1 < s2:
                gain_rate = new_gain_rate
            else:
                time += s2
                break
        
        return time
        
        
        
        
if __name__ == '__main__':
    fname = os.path.join(paths.DATA_DIR, 'Qualification_2014/B-large.in')
    lines = open(fname).readlines()
    num_problems = int(lines[0])
    
    i = 1
    case_id = 1
    while i < len(lines):
        [C, F, X] = [float(x) for x in lines[i].strip().split()]
        
        problem = CookieClicker(C, F, X)
        result = problem.solve()
        print 'Case #%d: %.7f' % (case_id, result)
        
        case_id += 1
        i += 1