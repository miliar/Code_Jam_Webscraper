__author__ = 'avital'

def all_up(pancakes):
    for pancake in pancakes:
        if pancake == '-':
            return False
    return True

def flipper_count(pancakes, flips, index, count):
    # import pdb; pdb.set_trace()

    if all_up(pancakes):
        return count
    if pancakes[index] == '+':
        return flipper_count(pancakes, flips, index+1, count)
    if index > len(pancakes) - flips:
        return 100000000
    return flipper_count(flip(pancakes, flips, index), flips, index+1, count+1)

def flip(pancakes, flips, index):
    pancakes_temp = list(pancakes)
    for flip in range(0, flips):
        if(pancakes_temp[flip+index]) == '-':
            pancakes_temp[flip+index] = '+'
        else:
            pancakes_temp[flip+index] = '-'

    return "".join(pancakes_temp)


def main():
    with open('small.in', 'r') as small_input:
        with open('small_solution.txt', 'w') as small_output:
            cases = int(small_input.readline())
            for case in range(1, cases+1):
                row = small_input.readline().rstrip()
                pancakes = row.split()[0]
                flips = int(row.split()[1])
                # import pdb; pdb.set_trace()
                min_flips = flipper_count(pancakes, flips, 0, 0)
                if min_flips == 100000000:
                    min_flips = 'IMPOSSIBLE'
                print "Case " + str(case)
                small_output.write("Case #{case}: {min_flips}\n".format(case=case, min_flips=min_flips))

if __name__ == '__main__':
    main()