import sys

def rollercoaster_revenues(R, k, groups):
    
    total_revenue = 0
    transitions = [-1] * len(groups)
    revenues = [0] * len(groups)
    
    for i in range(len(groups)):
        revenues[i] = groups[i]
        j = (i + 1) % len(groups)
        while True:
            if j == i:
                transitions[i] = j
                break
            else:
                #print i, j, len(revenues), len(groups)
                if revenues[i] + groups[j] <= k:
                    revenues[i] += groups[j]
                else:
                    transitions[i] = j
                    break
                
            j = (j + 1) % len(groups)
            
    #print transitions
    #print revenues
    
    visited = [False] * len(groups)
    history = []
    cur_group = 0
    cycle_revenues = 0
    cur_round = 0
    last_rounds = False
    
    while True:
        
        #print 'cur_round', cur_round
        
        if cur_round == R:
            break
        
        
        elif visited[cur_group] and not last_rounds:
            
            cycle_history = history[history.index(cur_group):]
            for group in cycle_history:
                cycle_revenues += revenues[group]
            jumps = (R - cur_round)/len(cycle_history)
            total_revenue += jumps * cycle_revenues
            cur_round += jumps * len(cycle_history)
            
            #print 'found cycle', cycle_history, 'revenues', cycle_revenues
                
            last_rounds = True
            
        else:
            if not visited[cur_group]:
                visited[cur_group] = True
                history.append(cur_group)
            
            #print 'group %s->%s and adding $%s to total %s' % (cur_group, transitions[cur_group], revenues[cur_group], total_revenue) 
            total_revenue += revenues[cur_group]
            cur_group = transitions[cur_group]
            
            
            cur_round += 1
    
     
    
    return total_revenue


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(1, T+1):
        R, k, N = map(int, sys.stdin.readline().split())
        groups = map(int, sys.stdin.readline().split())
        
        print 'Case #%s: %s' %  (i, rollercoaster_revenues(R, k, groups))
