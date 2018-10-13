import os

__author__ = 'Roberto'
import math

def get_result(camerons, jamies):

    camerons = [(True, tuple(map(int, times.split()))) for times in camerons]
    jamies = [(False, tuple(map(int, times.split()))) for times in jamies]
    all_time = camerons + jamies

    all_time.sort(key=lambda t: t[1])
    print(all_time)
    switch_time = []
    own_time = []

    prev_end = all_time[-1][1][1]
    prev_who = all_time[-1][0]
    for who, times in all_time:
        start, end = times
        diff = (start - prev_end) % 1440

        if diff > 0:
            if prev_who == who:
                own_time.append((who, diff))
            else:
                switch_time.append(diff)

        prev_end = end
        prev_who = who

    print(switch_time)
    print(own_time)

    all_cameron = sum([times[1] - times[0] for who, times in camerons]) + sum(time for who, time in own_time if who)
    all_jamies = sum([times[1] - times[0] for who, times in jamies]) + sum(time for who, time in own_time if not who)
    print(all_cameron, all_jamies)

    larger = max(all_cameron, all_jamies)
    if larger <= 720:
        if all_time[0][0] == all_time[-1][0]:
            return len(all_time) - 1
        else:
            return len(all_time)



    # if any(who for who, times in all_time) and not all(who for who, times in all_time) and all_switch_time >= extra:
    #     if all_time[0][0] == all_time[-1][0]:
    #         return len(all_time) - 1
    #     else:
    #         return len(all_time)

    extra = larger - 720
    switches = 0
    who = larger == all_cameron

    larger_own_time = [diff for who2, diff in own_time if who == who2]
    larger_own_time.sort(reverse=True)
    for diff in larger_own_time:
        extra -= diff
        switches += 2
        if extra <= 0:
            break

    default_switches = 0
    prev_who = all_time[-1][0]
    for who, times in all_time:
        if who != prev_who:
            default_switches += 1
        prev_who = who

    print(default_switches)
    return default_switches + switches

def solve_test(index, *args):

    debug_out.write("Case #{0} In: {1} Out: ".format(index, args))

    print("Case: [{0}]".format(args))

    solution = get_result(*args)

    print(solution)

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def get_single_section():
    pass

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
            file_name = "{0}-small-attempt{1}.in".format(task, attempts)
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
        c, j = map(int, test_cases[iter].split())
        iter+=1
        iter = get_input_section(test_cases, iter, c, params)
        iter = get_input_section(test_cases, iter, j, params)

        solve_test(i, *params)

    file_out.close()