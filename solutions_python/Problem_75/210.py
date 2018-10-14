import sys

num_cases = int(sys.stdin.readline())


def get_combos(rules):
    res = {}
    for e1, e2, c in rules:
        res[(e1, e2)] = c
        res[(e2, e1)] = c
    return res


def get_bombs(rules):
    res = {}
    for e1, e2 in rules:
        e1_bombs = res.get(e1, set())
        e1_bombs.add(e2)
        res[e1] = e1_bombs
        e2_bombs = res.get(e2, set())
        e2_bombs.add(e1)
        res[e2] = e2_bombs
    return res


def invoke(elements, combos, bombs):
    e_list = []
    e_hash = {}
    last_e = None
    for e in elements:
        if last_e:
            new_e = combos.get((e, last_e))
            if new_e:
                e = new_e
                e_list.pop()
                last_e_count = e_hash.get(last_e, 0) - 1
                if last_e_count < 1:
                    del e_hash[last_e]
                else:
                    e_hash[last_e] = last_e_count
                
        e_bombs = bombs.get(e)
        if e_bombs and (set(e_hash.keys()) & e_bombs):
            e_list = []
            e_hash = {}
            last_e = None
        else:
            e_list.append(e)
            e_hash[e] = e_hash.get(e, 0) + 1
            last_e = e
    return e_list
    

for j in xrange(num_cases):
    input = sys.stdin.readline().split()
    C = int(input[0])
    combos = get_combos(input[1:1+C])
    D = int(input[1+C])
    bombs = get_bombs(input[2+C:2+C+D])
    N = int(input[2+C+D])
    elements = input[3+C+D]
    if (3+C+D) != (len(input) - 1):
        raise Exception("input format error")
        
    res = invoke(elements, combos, bombs)
    print "Case #%s: [%s]" % (j+1, ', '.join(res))
    j += 1
