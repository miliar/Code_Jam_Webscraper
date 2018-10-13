import sys
import math
import itertools

def bad_add_list(int_list):
    # Convert all the decimals into binary strings without prefix
    binary_list = [bin(number)[2:] for number in int_list]
    
    total = binary_list.pop(0)

    for next_num in binary_list:
        total = bad_add(total, next_num)

    return int(total, 2)

def bad_add(b1, b2):
    # Zero pad them if necesary
    lb1, lb2 = len(b1), len(b2)
    if not lb1 == lb2:
        if lb1 < lb2:
            b1 = b1.zfill(lb2)
        else:
            b2 = b2.zfill(lb1)
    
    result = ''

    for a, b in zip(b1, b2):
        a, b = int(a), int(b)
        if (a, b) == (1, 1) or (a, b) == (0, 0):
            result += '0'
        else:
            result += '1'

    return result

def possible_selections(length):
    L = [i for i in range(length)]

    selections = []
    for i in range(1, int(math.floor(length/2.0))+1):
        for selection in itertools.combinations(L, i):
            selections.append(selection)

    return selections

if __name__ == '__main__':
    in_path = sys.argv[1]
    with open(in_path, 'r') as in_file:
        in_file.next()
        case = 1

        for i, line in enumerate(in_file):
            if (i+1)%2 == 0:
                solution = None
                sweets = [int(sweet) for sweet in line.split()]
                pos_sel = possible_selections(len(sweets))
                
                for selection in pos_sel:
                    sweets1 = []
                    sweets2 = sweets[:]
                    for i in selection:
                        sweets1.append(sweets2[i])
                        sweets2[i] = None
                    sweets2 = [sweet for sweet in sweets2 if sweet != None]
                    
                    if bad_add_list(sweets1) == bad_add_list(sweets2):
                        sum1, sum2 = sum(sweets1), sum(sweets2)
                        best_pile = sum1 if sum1 >= sum2 else sum2
                        if best_pile > solution:
                            solution = best_pile
            
                if not solution:
                    solution = 'NO'

                print "Case #%s: %s" % (case, solution)
                case += 1