import sys
from collections import defaultdict

DEBUG = True

def build_graph(root_keys, chests):
    graph = {}
    inverse_graph = defaultdict(list)
    graph[0] = [ch[0] for ch in chests if ch[1] in root_keys]
    for key in root_keys:
        for c in [ch for ch in chests if ch[1] == key]:
            inverse_graph[c[0]].append(0)
    for chest in chests:
        for key in chest[3]:
            for c in [ch for ch in chests if ch[1] == key and ch[0] != chest[0]]:
                inverse_graph[c[0]].append(chest[0])
        graph[chest[0]] = [ch[0] for ch in chests if ch[1] in chest[3]]
    return graph, inverse_graph

def backtrack(n, keys, chest_dict, opened_chests, graph, inv_graph):
    # try some naive combinatorial search with a bit of pruning
    if len(opened_chests) == n:
        return opened_chests
    if len(keys) == 0:
        return None
    candidate_chests = []
    for key in keys:
        if keys[key] > 0:
            candidate_chests += chest_dict[key]
    if len(candidate_chests) == 0:
        return None
    candidate_chests.sort(key=lambda x: x[0])
    while candidate_chests:
        next_chest = candidate_chests.pop(0)
        continue_while = False
        for c in candidate_chests:
            if c[1] == next_chest[1]:
                if len(inv_graph[c[0]]) == 1:
                    if len(inv_graph[next_chest[0]]) == 1:
                        return None
                    else:
                        debug('using pruning')
                        continue_while = True
                        break
        if continue_while:
            continue
        opened_chests.append(next_chest[0])
        keys[next_chest[1]] -= 1
        chest_dict[next_chest[1]].remove(next_chest)
        for key_idx in next_chest[3]:
            if key_idx not in keys:
                keys[key_idx] = 0
            keys[key_idx] += 1
        path = backtrack(n, keys, chest_dict, opened_chests, graph, inv_graph)
        if path is not None:
            return path
        opened_chests.pop()
        chest_dict[next_chest[1]].append(next_chest)
        keys[next_chest[1]] += 1
        for key_idx in next_chest[3]:
            keys[key_idx] -= 1
    return None

def solver(k, n, keys, chests):

    # sort by chest type
    # sanity check to make sure we have enough keys
    all_keys_dict = defaultdict(lambda: 0)
    for key in keys:
        all_keys_dict[key] += 1
    for chest in chests:
        for key in chest[3]:
            all_keys_dict[key] += 1
    chest_type_dict = defaultdict(lambda: 0)
    for chest in chests:
        chest_type_dict[chest[1]] += 1
    for t in chest_type_dict:
        if all_keys_dict[t] < chest_type_dict[t]:
            return 'IMPOSSIBLE'

    graph, inv_graph = build_graph(keys, chests)
    debug(graph)
    debug(inv_graph)
    chest_dict = defaultdict(list)
    for chest in chests:
        chest_dict[chest[1]].append(chest)
    for chest_type, chests_list in chest_dict.items():
        chests_list.sort(key=lambda x: x[0])
    key_dict = {}
    for key in keys:
        if key not in key_dict:
            key_dict[key] = 0
        key_dict[key] += 1
    path = backtrack(n, key_dict, chest_dict, [], graph, inv_graph)
    if path is None:
        return 'IMPOSSIBLE'
    else:
        return ' '.join([str(i) for i in path])

def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        k, n = ssi(rl())
        keys = ssi(rl())
        chests = []
        for i in range(n):
            chest_vals = ssi(rl())
            ti = chest_vals[0]
            ki = chest_vals[1]
            chest_keys = chest_vals[2:]
            chests.append((i+1, ti, ki, chest_keys))
        answer = solver(k, n, keys, chests)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
