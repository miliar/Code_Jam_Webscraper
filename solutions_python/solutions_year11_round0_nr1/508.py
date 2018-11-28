'''
Created on 06/05/2011

@author: German
'''
import math

def move(dest, position):
    if dest[1] != position[dest[0]]:
        dir = math.copysign(1,  dest[1]-position[dest[0]])
        position[dest[0]] += dir

def do_next(next, next_ot, position):
    steps=1
    while next[1] != position[next[0]]:
        move(next, position)
        if next_ot is not None:
            move(next_ot, position)
        steps+=1

    #Mientras presiona el boton, tiene uno mas        
    if next_ot is not None:
            move(next_ot, position)
        
    return steps
        
    
    

def sim_robots(case, position):
    if len(case) == 0:
        return 0
    next = case[0]
    ot_robot = [x for x in case[1:] if x[0]!=next[0]]
    next_ot = ot_robot[0] if len(ot_robot) >0 else None
    steps = do_next(next, next_ot, position)
    return steps + sim_robots(case[1:],position)
    
    
    
    

if __name__ == '__main__':
    with open('sol.out', 'w') as out:
        with open('A-large.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                case = f.readline().split()
                N = int(case[0])
                parsed_case = []
                for k in range(N):
                    parsed_case.append((case[1+2*k], int(case[2*k+2])))
                    
                res = sim_robots(parsed_case, {'B':1 ,'O': 1})
                res_str = "Case #%d: %d\n" % (i, res)
                print res_str,
                out.write(res_str)
            
            
            
            