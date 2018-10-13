
def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputA.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while (case<=no_cases):
        intervals = int(lines[2*case-1])
        mushroom_counts = [int(x) for x in lines[2*case].strip().split()]
        min1, min2 = get_solution(intervals, mushroom_counts)
        print "Case #{0}: {1} {2}".format(case, min1, min2)
        case += 1


def get_solution(intervals, mushroom_counts):
    diff_list = []
    for x in xrange(0, intervals-1):
        diff_list.append(mushroom_counts[x+1] - mushroom_counts[x])
    first_method_min = -sum([y for y in diff_list if y < 0])
    min_eating = min(diff_list)
    if min_eating < 0:
        constant_rate = -min_eating
    else:
        constant_rate = 0
    second_method_min = 0
    for index in xrange(0, intervals-1):
        if mushroom_counts[index] >= constant_rate:
             second_method_min += constant_rate
        else:
             second_method_min += mushroom_counts[index]
    return first_method_min, second_method_min



print_ouput()

