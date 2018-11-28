import os

__author__ = 'Roberto'
import math

def evenly_increase(units, u):

    if len(units) == 0:
        return []
    if len(units) == 1:
        units[0] += u
        return [min(1, units[0])]

    while u > 0:

        min_val = min(units)
        units_to_inc = [i for i in range(len(units)) if units[i] == min_val]
        others = [unit for unit in units if unit > min_val]
        if len(others) == 0:
            second_largest = 1
        else:
            second_largest = min(others)

        diff = second_largest - min_val

        if u < diff * len(units_to_inc):
            inc = u / len(units_to_inc)
            for i in units_to_inc:
                units[i] += inc

            return units
        else:
            for i in units_to_inc:
                units[i] += diff

            u -= diff * len(units_to_inc)

        if all(unit >= 1.0 for unit in units):
            return units
    return units

def get_result(k, u, units):

    n = len(units)

    if n > k:
        units.sort(reverse=True)
        top_units = units[:k]
        print(top_units)

        if u > 0:
            new_units = evenly_increase(top_units, u) + units[k:]
            print("new", new_units)
        else:
            new_units = units

        prob = 1
        for unit in new_units:
            prob *= (1 - unit)
        return 1 - prob

    else:
        new_units = evenly_increase(units, u)
        print("evenly", new_units)
        prob = 1
        for unit in new_units:
            prob *= unit

        return prob

def solve_test(index, *args):

    debug_out.write("Case #{0} In: {1} Out: ".format(index, args))

    print("Case: [{0}]".format(args))

    solution = get_result(*args)

    print(solution)

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def get_input_section(input_lines, iter, length, params):

        lines = test_cases[iter: iter + length]
        params.append(lines)
        return iter + length

if __name__ == "__main__":
    task = os.path.basename(os.path.dirname(__file__))
    level = 1
    attempts = 0
    practice = False

    if practice:
        if level == 0:
            file_name = "sample.in"
        elif level == 1:
            file_name = "{0}-small-practice.in".format(task, attempts)
        else:
            file_name = "{0}-large-practice.in".format(task)
    else:
        if level == 0:
            file_name = "sample.in"
        elif level == 1:
            file_name = "{0}-small-1-attempt{1}.in".format(task, attempts)
        else:
            file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]
    iter = 0
    for i in range(0, number_of_lines):

        params = []

        n, k = map(int, test_cases[iter].split())
        iter+=1
        params.append(k)
        u = float(test_cases[iter])
        iter+=1
        params.append(u)
        nums = list(map(float, test_cases[iter].split()))
        iter+=1
        params.append(nums)

        solve_test(i, *params)

    file_out.close()