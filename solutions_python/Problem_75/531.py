'''
Created on 07/05/2011

@author: German
'''

def reduce(game, combinations, oppositions):
    if len(game) < 2:
        return
    
    for rule in combinations:
        if (rule[0] == game[-1] and rule[1] == game[-2]) or \
            (rule[1] == game[-1] and rule[0] ==  game[-2]):
            
                
            game[-2:] = [rule[2]]
            return
    
    for rule in oppositions:
        if (rule[0] == game[-1] and rule[1] in game[:-1]) or \
            (rule[1] == game[-1] and rule[0] in game[:-1]):
            game[:] = [] 
            return
        
    
           

def play(case):
    played = []
    for c in case['plays']:
        played.append(c)
        reduce(played, case['combinations'], case['oppositions'])
    
    return played


if __name__ == '__main__':
    with open('sol.out', 'w') as out:
        with open('B-large.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                case = f.readline().split()
                parsed_case = {'combinations':[], 'oppositions': [], 'plays': []}
                
                C = int(case[0])
                case = case[1:]
                for k in range(C):
                    parsed_case['combinations'].append((case[0][0],case[0][1],case[0][2]))
                    case = case[1:]
                
                D = int(case[0])
                case = case[1:]
                for k in range(D):
                    parsed_case['oppositions'].append((case[0][0],case[0][1]))
                    case = case[1:]
                
                N = int(case[0])
                case = case[1:]
                parsed_case['plays'] = [c for c in case[0]]
                    
                    
                res = play(parsed_case)
                
                res_str = "Case #%d: %s\n" % (i, '['+', '.join(res)+']')
                print res_str,
                out.write(res_str)