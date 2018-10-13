__author__ = 'cwagner'

import sys

def speciaal_time(value, div):
    if div >= value:
        return [1 for i in range(value)]
    dividende = value / div
    new_list = [dividende for i in range(div)]
    for i in range(value % div):
        new_list[i] += 1
    return new_list

def resolve_case(nb_plates, nb_pancakes):
    best_score = max(nb_pancakes)
    worse = best_score

    copy_list = [[i] for i in nb_pancakes]
    max_value = max([(i, max(val), len(val)) for i, val in enumerate(copy_list)], key=lambda p: p[1])
    spe_min = 0
    while max_value[1] > 3:
        default_value = nb_pancakes[max_value[0]]
        copy_list[max_value[0]] = speciaal_time(default_value, max_value[2] + 1)
        max_value = max([(i, max(val), len(val)) for i, val in enumerate(copy_list)], key=lambda p: p[1])
        score = reduce(lambda a, b: a + len(b) if len(b) > 1 else a, copy_list, 0) - len([1 for x in copy_list if len(x) > 1]) + max_value[1]
        spe_min += 1
        if score < best_score:
            best_score = score
        if spe_min >= worse:
            break
    return best_score

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        line = [i for i in f.readlines() if i[0] != '#']
        tests = ((len(line) - 1) / 2)
        i = 1
        for x in range(tests):
            time = resolve_case(int(line[(x * 2) + 1]), [int(x) for x in (line[((x+1) * 2)].split())])
            print "Case #{}: {}".format(i, time)
            i += 1
    return


if __name__ == '__main__':
    main()
