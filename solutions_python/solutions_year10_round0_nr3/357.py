#!/usr/bin/env python


def get_cycle_length_and_value(queue, capacity, value_start_index):
    rounds = 0
    index = 0
    income = 0
    aux_list = []
    ammount_dict = {}
    while index not in aux_list:
        aux_list.append(index)
        index = value_start_index[index][1]
    i = aux_list.index(index)
    while i < len(aux_list):
        rounds += 1
        income += value_start_index[aux_list[i]][0]
        i += 1
    
    return index, rounds, income

if __name__ == '__main__':
    
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        R, k, N = map(int, raw_input().split(' '))
        queue = map(int, raw_input().split(' '))
        cost_dict = {}
        for j in xrange(N):
            sum = 0
            i2 = j
            while sum + queue[i2] <= k:
                sum += queue[i2]
                i2 = (i2 + 1) % N
                if i2 == j:
                    break
            cost_dict[j] = (sum, i2)
        index_cycle, rounds_cycle, income_cycle = get_cycle_length_and_value(queue, k, cost_dict)
        index = 0
        income = 0
        while R > 0 and index != index_cycle:
            income += cost_dict[index][0]
            index = cost_dict[index][1]
            R -= 1
        income += (R / rounds_cycle) * income_cycle
        R %= rounds_cycle
        while R > 0:
            income += cost_dict[index][0]
            index = cost_dict[index][1]
            R -= 1
        print "Case #%d: %ld" % (i+1, income)

    