
def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        (a, b) = map(int, fh.readline().strip().split())
        prob = map(float, fh.readline().strip().split())
        test_data[count] = (a, b, prob)
        count = count + 1

    fh.close()
    return test_data

def permute_prob(l):
    if len(l) == 0:
        return []
    
    if len(l) == 1:
        return [[l[0]], [1 - l[0]]]

    possible_lists = []
    small_pl = permute_prob(l[1:])

    for tl in small_pl:
        nl = [l[0]]
        nl.extend(tl)
        possible_lists.append(nl)

        nl = [1 - l[0]]
        nl.extend(tl)
        possible_lists.append(nl)

    return possible_lists 

def permute_words(l):
    if len(l) == 0:
        return []
    
    if len(l) == 1:
        return [['r'], ['w']]

    possible_lists = []
    small_pl = permute_words(l[1:])

    for tl in small_pl:
        nl = ['r']
        nl.extend(tl)
        possible_lists.append(nl)

        nl = ['w']
        nl.extend(tl)
        possible_lists.append(nl)

    return possible_lists 

def _execute_test(test_data):
    (a, b, prob) = test_data

    assert len(prob) == a
    words = ['r'] * a
    possible_words = permute_words(words)
    possible_probs = permute_prob(prob)
    
    enter_cost = 1
    bk_cost = 1
    
    print a, b, prob

    final_costs = list()
    for (i, case) in enumerate(possible_words):
        case_value = reduce(lambda x, y: x * y, possible_probs[i])
        wrong_case = False
        if 'w' in case:
            wrong_case = True
        case_cost = []
        
        # Keep Typing
        c1 = b - a + enter_cost
        if wrong_case:
            c1 += b + enter_cost
        
        case_cost.append(c1 * case_value)
        
        # Press Enter
        c2 = enter_cost + b + enter_cost
        case_cost.append(c2 * case_value)
        
        wrong_idx = -1
        try:
            wrong_idx = case.index('w')
        except ValueError:
            pass

        cb = list()
        # Press backspaces
        for nb in range(1, a+1):
            tmp_cost = nb * bk_cost
            tmp_cost += nb + (b - a) + enter_cost
             
            reached_idx = a - nb
            if (wrong_idx != -1) and (reached_idx > wrong_idx):
                tmp_cost += b + enter_cost

            cb.append(tmp_cost)
            case_cost.append(tmp_cost * case_value)

        #print "*** ", case, case_value, c1, c2, cb, case_cost
        final_costs.append(case_cost)
        
    #print final_costs
    best_cost = min([sum(pair) for pair in zip(*final_costs)])
    return '%.6f' % best_cost

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))

    output.close()

if __name__ == '__main__':
    main()