#!/usr/bin/python3


def check_combine(element_list, combinations, element):
    last = element_list[-1]
    if last == element:
        last_two = last + element.lower()
    else:
        last_two = last + element
    c = combinations.get(frozenset(last_two), None)
    if c:
        del(element_list[-1])
        element_list.append(c)
        return True
    return False

def interpret_case(case):
    combinations = {}
    invokations = set()
    element_list = []
    c = int(case.pop(0))
    for i in range(c):
        comb = case.pop(0)
        if comb[0] == comb[1]:
            comb = comb[0] + comb[1].lower() + comb[2]
        combinations[frozenset(comb[0:2])] = comb[2]
    n = int(case.pop(0))
    for i in range(n):
        invok = case.pop(0)
        invokations.add(frozenset(invok))
    case.pop(0) # size of str
    elements = case.pop(0)
    for element in elements:
        if len(element_list) >= 1:
            done = check_combine(element_list, combinations, element)
            if not done:
                for each in element_list:
                    poss = each + element
                    if frozenset(poss) in invokations:
                        element_list = []
                        break
                if element_list:
                    element_list.append(element)
        else:
            element_list.append(element)
    return element_list

def main():
    cases = int(input())
    for i in range(cases):
        case = input()
        print('Case #{0}: '.format(i+1), end='')
        l_end = interpret_case(case.split())
        print('[',end='')
        for i in l_end[:-1]:
            print(i, ',' , sep='', end=' ')
        if l_end:
            print('{0}'.format(l_end[-1]), end='')
        print(']')


if __name__ == '__main__':
    main()
