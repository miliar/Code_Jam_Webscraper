import math

def write_solutions(solutions):
    f = open('prob_B_large.output', 'w')
    for i, sol in enumerate(solutions):
        f.write('Case #%d: %d\n' % ((i + 1), sol))
    f.close()



def solve_cases(cases):
    for j, case in enumerate(cases):
        print 'solving %d' % (j + 1)
        print case
        yield solve_case(case)


def solve_case(case):
    return solve_B(case[0][0], case[0][1], case[1], case[2])


def solve_B(Ac, Aj, Ac_ints, Aj_ints):
    combined_ints = Ac_ints + Aj_ints
    forced, unforced = get_forced_and_unforced_intervals(combined_ints)
    Aj_forced = sum([x[2] - x[1] for x in Ac_ints])
    Ac_forced = sum([x[2] - x[1] for x in Aj_ints])
    Aj_unforced = sum([x[2] - x[1] for x in unforced if x[0] == 'j'])
    Ac_unforced = sum([x[2] - x[1] for x in unforced if x[0] == 'c'])
    Aj_needed = 720 - Aj_forced - Aj_unforced
    Ac_needed = 720 - Ac_forced - Ac_unforced
    num_forced = len(forced)
    forced_slack = sum([x[3] - x[2] for x in forced])
    if can_solve(Aj_needed, Ac_needed, forced_slack):
        return num_forced
    least_needed = max(0, min(Aj_needed, Ac_needed))
    unforced.sort(key=lambda x: -(x[2] - x[1]))
    who_needs = 'j' if Aj_needed > 0 else 'c'
    how_much = max(Aj_needed, Ac_needed)
    how_much -= (forced_slack - least_needed)
    swaps = num_forced
    for interval in unforced:
        if interval[0] == who_needs:
            continue
        max_time = interval[2] - interval[1]
        how_much -= max_time
        swaps += 2
        if how_much <= 0:
            return swaps



def can_solve(Aj_needed, Ac_needed, forced_slack):
    if forced_slack < Aj_needed:
        return False
    forced_slack -= max(Aj_needed, 0)
    if forced_slack < Ac_needed:
        return False
    return True

# forced is (from person, to person, from time, to time)
# unforced is (holding person, from time, to time)

def get_forced_and_unforced_intervals(ints):
    ints.sort(key=lambda x: x[1])
    earliest_int = ints[0]
    latest_int = ints[-1]
    last_person = None

    forced = []
    unforced = []
    for j, interval in enumerate(ints):
        if last_person is None:
            last_person = interval[0]
            if latest_int[2] == 1440 and earliest_int[1] == 0:
                if latest_int[0] == earliest_int[0]:  # same person, can't swap
                    continue
                else: # different person, must swap
                    forced.append((earliest_int[0], latest_int[0], latest_int[2] - 1440, earliest_int[1]))
                    continue
            if latest_int[0] == earliest_int[0]:  # same person across midnight
                unforced.append((opposite_person(latest_int[0]), latest_int[2] - 1440, earliest_int[1]))
            else:  # diff people across midnight
                forced.append((earliest_int[0], latest_int[0], latest_int[2] - 1440, earliest_int[1]))
            continue
        if last_person != interval[0]:  # forced switch
            forced.append((interval[0], last_person, ints[j - 1][2], interval[1]))
            last_person = interval[0]
        else:
            prev_end = ints[j - 1][2]
            if prev_end < interval[1]:
                unforced.append((opposite_person(last_person), prev_end, interval[1]))
    return forced, unforced


def opposite_person(person):
    if person == 'c':
        return 'j'
    return 'c'


def parse_input(stream):
    num_cases = None
    test_cases = []
    in_test_case = False
    cur_Ac = None
    cur_Aj = None
    Ac_left = None
    Aj_left = None
    cur_test_case = []
    cur_person = None
    for i, line in enumerate(stream):
        if i == 0:
            num_cases = int(line.strip())
            in_test_case = False
            continue
        if not in_test_case:
            cur_Ac, cur_Aj = line.strip().split(' ')
            cur_Ac = int(cur_Ac)
            cur_Aj = int(cur_Aj)
            in_test_case = True
            Ac_left = cur_Ac
            Aj_left = cur_Aj
            cur_test_case.append((cur_Ac, cur_Aj))
            cur_test_case.append([])
            cur_person = 'c'
            if Ac_left == 0:
                cur_person = 'j'
                cur_test_case.append([])
            continue
        start, end = line.strip().split(' ')
        start = int(start)
        end = int(end)
        cur_test_case[-1].append((cur_person, start, end))
        if cur_person == 'c':
            Ac_left -= 1
            if Ac_left == 0:
                if Aj_left == 0:
                    cur_person = None
                    cur_test_case.append([])
                else:
                    cur_person = 'j'
                    cur_test_case.append([])
        else:
            Aj_left -= 1
            if Aj_left == 0:
                cur_person = None
        if cur_person is None:
            test_cases.append(cur_test_case)
            in_test_case = False
            cur_test_case = []

    return test_cases


if __name__ == '__main__':
    f = open('/Users/jakemagner/Desktop/google_code_jam/r1/B-large.in')
    # f = open('/Users/jakemagner/Desktop/google_code_jam/r1/probA_example.inp')
    cases = parse_input(f)
    write_solutions(solve_cases(cases))
