'''
Created on 2014-04-11

@author: Wei
'''
import os.path
import paths

class MagicTrick:
    def __init__(self, ans1, rows1, ans2, rows):
        self.ans1 = ans1
        self.grid1 = []
        for row in rows1:
            self.grid1.append([int(x) for x in row.strip().split()])
        
        self.ans2 = ans2
        self.grid2 = []
        for row in rows2:
            self.grid2.append([int(x) for x in row.strip().split()])
    
    
    def solve(self):
        intersection = set(self.grid1[self.ans1 - 1]).intersection(set(self.grid2[self.ans2 - 1]))
        
        if len(intersection) == 1:
            return str(list(intersection)[0])
        elif len(intersection) == 0:
            return 'Volunteer cheated!'
        else:
            return 'Bad magician!'
        
        
if __name__ == '__main__':
    fname = os.path.join(paths.DATA_DIR, 'Qualification_2014/A-small-attempt0.in')
    lines = open(fname).readlines()
    num_problems = int(lines[0])
    
    i = 1
    case_id = 1
    while i < len(lines):
        ans1 = int(lines[i])
        rows1 = lines[i + 1 : i + 5]
        ans2 = int(lines[i + 5])
        rows2 = lines[i + 6 : i + 10]
        
        problem = MagicTrick(ans1, rows1, ans2, rows2)
        result = problem.solve()
        print 'Case #%d: %s' % (case_id, result)
        
        case_id += 1
        i += 10