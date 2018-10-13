'''
Created on 2014-04-11

@author: Wei
'''
import os.path
import paths

class War:
    def __init__(self, N, block_line1, block_line2):
        self.N = N
        self.blocks1 = sorted([float(x) for x in block_line1.strip().split()])
        self.blocks2 = sorted([float(x) for x in block_line2.strip().split()])

#        print 'Naomi', self.blocks1
#        print 'Ken', self.blocks2
        
    def solve_war_helper(self, blocks1, blocks2):
        if len(blocks1) == 0:
            return 0
        
        if blocks1[0] > blocks2[-1]:
            return len(blocks1)
        
        max_points = 0
#        max_comb = None
        b1 = blocks1[1 : ]
        for i in range(len(blocks2)):
            if blocks2[i] > blocks1[0]:
                break
                
        b2 = blocks2[ : i] + blocks2[i + 1 : ]
        #print blocks1[0], i, blocks2[i], b2
        p = self.solve_war_helper(b1, b2)
        if p > max_points:
#                max_comb = (b, blocks2[i])
            max_points = p
        
        if blocks1[-1] > blocks2[-1]:
            p = self.solve_war_helper(blocks1[ : -1], blocks2[1 : ]) + 1
            if p > max_points:
#                max_comb = (b, blocks2[i])
                max_points = p
        
#        if self.N > 3:
#            print blocks1
#            print blocks2
#            print max_comb
#            print
#        if len(blocks1) == self.N:
#            print blocks1
#            print blocks2
#            print max_comb
#            print
        return max_points
    
    def solve_war(self):
        
        return self.solve_war_helper(self.blocks1, self.blocks2)
    
    
    ''' assume blocks1 and blocks2 are sorted '''
    def solve_deceitful_war_helper(self, blocks1, blocks2):
#        print 'blocks1', blocks1
#        print 'blocks2', blocks2
        
        if len(blocks1) == 0:
            return 0
        
        if blocks1[0] > blocks2[-1]:
            return len(blocks1)
        
#        max_points = 0
##        max_comb = None
#        for i in range(len(blocks2)):
#            b2 = blocks2[ : i] + blocks2[i + 1 : ]
#            p = self.solve_deceitful_war_helper(blocks1[1 : ], b2)
#            if p > max_points:
##                max_comb = (b, blocks2[i])
#                max_points = p
#                
##            break
#
#        return max_points
        
        #print 'Naomi', 0.5*(blocks2[-1] + blocks2[-2])
        p1 = self.solve_deceitful_war_helper(blocks1[1 : ], blocks2[ : -1])
        p2 = self.solve_deceitful_war_helper(blocks1[1 : ], blocks2[1 : ])
        if blocks1[0] > blocks2[0]:
            p2 += 1
            
        return max(p1, p2)
    
    def solve_deceitful_war(self):
        return self.solve_deceitful_war_helper(self.blocks1, self.blocks2)

    def solve(self):
        p1 = self.solve_deceitful_war()
        p2 = self.solve_war()
        
        return p1, p2
    
    
if __name__ == '__main__':
    fname = os.path.join(paths.DATA_DIR, 'Qualification_2014/D-small-attempt2.in')
    lines = open(fname).readlines()
    num_problems = int(lines[0])
    
    i = 1
    case_id = 1
    while i < len(lines):
        N = int(lines[i])
        block_line1 = lines[i + 1]
        block_line2 = lines[i + 2]
        
        problem = War(N, block_line1, block_line2)
        p1, p2 = problem.solve()
        print 'Case #%d: %d %d' % (case_id, p1, p2)
        
        case_id += 1
        i += 3