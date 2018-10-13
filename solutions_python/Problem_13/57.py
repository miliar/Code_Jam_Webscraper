import sys, itertools

data = filter(None, map(lambda x:x.strip(), open(sys.argv[1]).readlines()))

def pop_int(data):
    return int(data.pop(0))

def pop_ints(data):
    return map(int, data.pop(0).split())

def pop_rows(data, num_rows):
    result = data[:num_rows]
    for i in range(num_rows):
        data.pop(0)
    return result

def pop_case(data):
    num_nodes, target = pop_ints(data)
    interior_nodes = []
    for i in range((num_nodes -1 )/2):
        gate, changeable = pop_ints(data)
        gate = ['OR', 'AND'][gate]
        node = (gate, changeable)
        interior_nodes.append(node)
    leaves = []
    for i in range((num_nodes + 1)/2):
        leaves.append(pop_int(data))
    return interior_nodes, leaves, target

CACHED_VALUES = {}

def node_value(pos, interior_nodes, leaves):
    # pos is 1-indexed
    if pos in CACHED_VALUES:
        return CACHED_VALUES[pos]
    elif pos <= len(interior_nodes):
        gate, change_null = interior_nodes[pos-1]
        l_child_pos = pos*2
        r_child_pos = pos*2 + 1
        if node_value(l_child_pos, interior_nodes, leaves):
            if gate == 'OR':
                CACHED_VALUES[pos] = True
                return True
            elif node_value(r_child_pos, interior_nodes, leaves):
                CACHED_VALUES[pos] = True
                return True
            else:
                CACHED_VALUES[pos] = False
                return False
        else:
            if gate == 'AND':
                CACHED_VALUES[pos] = False
                return False
            elif node_value(r_child_pos, interior_nodes, leaves):
                CACHED_VALUES[pos] = True
                return True
            else:
                CACHED_VALUES[pos] = False
                return False
    else:
        new_pos = pos - len(interior_nodes)
        val = leaves[new_pos - 1]
        CACHED_VALUES[pos] = val
        return val
    
def min_to_switch(pos, interior_nodes, leaves, target):
    val = node_value(pos, interior_nodes, leaves)
    #print pos, val
    if val == target:
        return 0
    if pos > len(interior_nodes):
        return 20000
    gate, changeable = interior_nodes[pos - 1]
    best = 20000
    l_child_pos = pos*2
    r_child_pos = pos*2 + 1
    if changeable:
        if gate == 'OR' and val:
            make_l_false = min_to_switch(l_child_pos, interior_nodes, leaves, False)
            make_r_false = min_to_switch(r_child_pos, interior_nodes, leaves, False)
            return 1 + min(make_l_false, make_r_false)
        elif gate == 'OR' and not val:
            make_l_true = min_to_switch(l_child_pos, interior_nodes, leaves, True)
            make_r_true = min_to_switch(r_child_pos, interior_nodes, leaves, True)
            return min(make_l_true, make_r_true)
        elif gate == 'AND' and val:
            make_l_false = min_to_switch(l_child_pos, interior_nodes, leaves, False)
            make_r_false = min_to_switch(r_child_pos, interior_nodes, leaves, False)
            return min(make_l_false, make_r_false)
        elif gate == 'AND' and not val:
            make_l_true = min_to_switch(l_child_pos, interior_nodes, leaves, True)
            make_r_true = min_to_switch(r_child_pos, interior_nodes, leaves, True)
            return 1 + min(make_l_true, make_r_true)
    else:
        if gate == 'OR' and val:
            make_l_false = min_to_switch(l_child_pos, interior_nodes, leaves, False)
            make_r_false = min_to_switch(r_child_pos, interior_nodes, leaves, False)
            return make_l_false + make_r_false
        elif gate == 'OR' and not val:
            make_l_true = min_to_switch(l_child_pos, interior_nodes, leaves, True)
            make_r_true = min_to_switch(r_child_pos, interior_nodes, leaves, True)
            return min(make_l_true, make_r_true)
        elif gate == 'AND' and val:
            make_l_false = min_to_switch(l_child_pos, interior_nodes, leaves, False)
            make_r_false = min_to_switch(r_child_pos, interior_nodes, leaves, False)
            return min(make_l_false, make_r_false)
        elif gate == 'AND' and not val:
            make_l_true = min_to_switch(l_child_pos, interior_nodes, leaves, True)
            make_r_true = min_to_switch(r_child_pos, interior_nodes, leaves, True)
            return make_l_true + make_r_true
    assert(False)
    
        
def solve(interior_nodes, leaves, target):
    #print "-"*30
    #print interior_nodes
    #print leaves
    #print target
    global CACHED_VALUES
    best = min_to_switch(1, interior_nodes, leaves, target)
    return best if best < 20000 else 'IMPOSSIBLE'
    
num_cases = pop_int(data)
for case_num in range(1, num_cases+1):
    answer = solve(*pop_case(data))
    CACHED_VALUES = {}
    print "Case #%d: %s" % (case_num, answer)
