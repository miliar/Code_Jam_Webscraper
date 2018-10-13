
def find_min_num_of_swaps(pancakes, K):
    '''
    :param pancackes: (list of strings) + is happy, - is blank pancake
    :param K: (int) - how much consecutive elements should we swap
    :return: minimum # of swaps, if no solutions (str) "IMPOSSIBLE"
    '''
    # Conver el-ts in list to Boolean
    res = 0
    pancakes = [True if el == '+' else False for el in pancakes]

    i = 0  # current key
    while i + 1 <= len(pancakes):
        # print pancakes, i, 'swaps:%s' % res

        if all(pancakes[i:i + K]):  # all are True, make a jump on K elements (step size)
            # print 'case 1'
            i += K
        elif pancakes[i] is True:
            # print 'case 2'
            i += 1
        elif pancakes[i] is False:
            if i + K > len(pancakes):  # swap goes out of bounds, exit
                # print 'case 3'
                res = 'IMPOSSIBLE'
                break
            else:  # swap consecutive el-ts + append tail
                # print 'case 4'
                flipped_elts = [not pancake for pancake in pancakes[i:i + K]]
                pancakes = flipped_elts + pancakes[i + K:]
                i = 1  # start from the second element
                # Increment total # of flips
                res += 1
    return res


results = []
with open('A-large.in', 'r') as f:
    t = int(f.readline())
    case = 1
    print t
    for line in f:
        print line
        pancakes, K = line.strip().split()

        # Run main function..
        res = find_min_num_of_swaps(pancakes, int(K))

        text = "Case #{}: {}".format(case, res)
        results.append(text); print text
        case += 1

with open('results.out', 'w') as f:
    f.write('\n'.join(results))
