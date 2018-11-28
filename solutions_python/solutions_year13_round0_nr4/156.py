'''
Created on 13.04.2013

@author: Great Combinator
'''

class KeyPath(object):
    def __init__(self, inp, outp):
        self.input_path = inp
        self.output_path = outp
        self.numberOfTCs = 0     
    
    def exclusive_way(self, key_type, unopened, full_chest_set):
        keys = {}
        for chest in unopened:
            if key_type in full_chest_set[chest]['keys']:
                keys[full_chest_set[chest]['key_type']] = None
        if len(keys) == 1 and keys.has_key(key_type):
            return True
        else:
            return False
        
    def get_possible_moves(self, keys, unopened, full_chest_set, necessary_keys, reachable_keys):
        possible = []
        for chest in unopened:
            if full_chest_set[chest]['key_type'] in keys:
                possible.append(chest)
        impossibles = []
        for way in possible:
            key_type = full_chest_set[way]['key_type']
            if (necessary_keys[key_type] > 1 
            and keys.count(key_type) == 1 
            and key_type not in full_chest_set[way]['keys']
            and self.exclusive_way(key_type, unopened, full_chest_set)):
                impossibles.append(way)
        for impossible in impossibles:
            idx = possible.index(impossible)
            del possible[idx]
        possible.sort()
        return possible
    
    def get_necessary_keys(self, unopened, full_chest_set):
        keys = {}
        for chest in unopened:
            keys[full_chest_set[chest]['key_type']] = 0
        for chest in unopened:
            keys[full_chest_set[chest]['key_type']] += 1
        return keys
    
    def get_reachable_keys(self, keys, unopened, full_chest_set):
        res_keys = {}
        for key in keys:
            res_keys[key] = 0
        for chest in unopened:
            for key in full_chest_set[chest]['keys']:
                res_keys[key] = 0
        
        for key in keys:
            res_keys[key] += 1
        for chest in unopened:
            for key in full_chest_set[chest]['keys']:
                res_keys[key] += 1
        return res_keys
    
    def get_path(self, keys, unopened, full_chest_set):
        if len(keys) == 0 and len(unopened) > 0:
            return ['IMPOSSIBLE']
            
        if len(unopened) == 1 and full_chest_set[unopened[0]]['key_type'] in keys:
            return [unopened[0]]
        
        #possible_moves = self.get_possible_moves(keys, unopened, full_chest_set)
        #if len(possible_moves) == 0:
        #    return ['IMPOSSIBLE']
        
        necessary_keys = self.get_necessary_keys(unopened, full_chest_set)
        reachable_keys = self.get_reachable_keys(keys, unopened, full_chest_set)
        for key in necessary_keys:
            if not reachable_keys.has_key(key) or reachable_keys[key] < necessary_keys[key]:
                return ['IMPOSSIBLE']
        
        possible_moves = self.get_possible_moves(keys, unopened, full_chest_set, necessary_keys, reachable_keys)
        if len(possible_moves) == 0:
            return ['IMPOSSIBLE']
        
        #print keys, unopened
        #print necessary_keys, reachable_keys
        idx = 0
        while idx < len(possible_moves):
            #print idx, len(unopened)
            new_keys = list(keys)
            new_keys.remove(full_chest_set[possible_moves[idx]]['key_type'])
            new_keys = new_keys + full_chest_set[possible_moves[idx]]['keys']
            new_keys.sort()
            new_unopened = list(unopened)
            new_unopened.remove(possible_moves[idx])
            path = [possible_moves[idx]] + self.get_path(new_keys, new_unopened, full_chest_set)
            
            if 'IMPOSSIBLE' not in path:
                return path
            idx += 1
        return ['IMPOSSIBLE']
        
    def solve(self):
        input_file = open(self.input_path, 'r')
        output_file = open(self.output_path, 'w')
        lines = input_file.readlines()
        self.numberOfTCs = int(lines[0].strip())
        
        line_idx = 1
        current_tc = 1
        while current_tc <= self.numberOfTCs:
            dimensions = [int(elem) for elem in lines[line_idx].strip().split(' ')]
            #print line_idx, lines[line_idx], dimensions
            nr_start_keys = dimensions[0]
            nr_chests = dimensions[1]
            line_idx += 1
            start_keys = [int(elem) for elem in lines[line_idx].strip().split(' ')]
            start_keys.sort()
            chests = {}
            idx = 1
            line_idx += 1
            while idx <= nr_chests:
                line_idx
                chests[idx] = {}
                chest_descr = [int(elem) for elem in lines[line_idx].strip().split(' ')]
                chests[idx]['key_type'] = chest_descr[0]
                chests[idx]['keys'] = chest_descr[2:]
                chests[idx]['keys'].sort()
                line_idx += 1
                idx += 1
            
            output_file.write('Case #%s: %s\n' % (current_tc, 
                                                  ' '.join([str(elem) for elem in self.get_path(start_keys, chests.keys(), chests)])))        
            #print current_tc, start_keys, chests 
            current_tc += 1
            
        input_file.close()
        output_file.close()            
            
def main():
    input_path = r'C:\Users\Great Combinator\workspace\GCJ2013\treasure\D-small-attempt2.in'
    output_path = r'C:\Users\Great Combinator\workspace\GCJ2013\treasure\D-small-attempt2.out'
    problem = KeyPath(input_path, output_path)
    problem.solve()
    
if __name__ == '__main__':
    main()