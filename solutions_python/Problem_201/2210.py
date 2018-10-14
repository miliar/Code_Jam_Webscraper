from math import floor, ceil


def get_min_max_from_run(run_length):
    return floor((run_length-1)/2), ceil((run_length-1)/2)


def pick_best_stall(stalls):
    encoded = []
    current_run = 0
    longest_run = 0
    longest_run_index = None
    for index, stall in enumerate(stalls):
        if stall == 1:
            if current_run > 0:
                encoded.append(current_run)
            encoded.append(0)
            if current_run > longest_run:
                longest_run = current_run
                longest_run_index = index - longest_run  # this is the starting point of the run
            current_run = 0
        else:
            current_run += 1

    min_gaps, max_gaps = get_min_max_from_run(longest_run)
    best_stall = longest_run_index + min_gaps

    return best_stall, min_gaps, max_gaps


def pick_stall(stalls):
    stalls[pick_best_stall(stalls)[0]] = 1


def solve_old(n, k):
    stalls = [1] + [0] * n + [1]
    for _ in range(k-1):
        pick_stall(stalls)

    _, min_gap, max_gap = pick_best_stall(stalls)

    return min_gap, max_gap


def create_runs(stalls):
    runs = [0]*(len(stalls)-2)
    current_run = 0
    longest_run = 0
    for index, stall in enumerate(stalls):
        if stall == 1:
            if current_run > 0:
                runs[current_run - 1] += 1
                longest_run = max(current_run, longest_run)
            current_run = 0
        else:
            current_run += 1

    return runs, longest_run


def update_runs(runs, longest_run):
    runs[longest_run-1] -= 1
    to_increase_low = floor((longest_run - 1) / 2) - 1
    to_increase_high = ceil((longest_run - 1) / 2) - 1
    if to_increase_low >= 0:
        runs[to_increase_low] += 1
    if to_increase_high >= 0:
        runs[to_increase_high] += 1

    if runs[longest_run-1] == 0:
        while longest_run > 0:
            longest_run -= 1
            if runs[longest_run-1] > 0:
                break

    return longest_run

def solve(n, k):
    stalls = [1] + [0] * n + [1]

    runs, longest_run = create_runs(stalls)
    for _ in range(k-1):
        longest_run = update_runs(runs, longest_run)

    min_gaps = floor((longest_run - 1) / 2)
    max_gaps = ceil((longest_run - 1) / 2)

    return min_gaps, max_gaps

if __name__ == "__main__":
    file_in = 'C-small-2-attempt0.in'
    with open(file_in) as f:
        input = f.read().splitlines()

    t = int(input[0])
    # t = int(input())

    output = ''

    for case_no in range(t):
        print(case_no)
        # pancakes, k = parse(input[case_no+1])
        # n = int(input())
        # k = int(input())
        n, k = input[case_no+1].split(' ')
        n = int(n)
        k = int(k)
        # print("Case #{}: {}".format(case_no + 1, solve(n)))
        solution = solve(n, k)
        output += "Case #{}: {} {}\n".format(case_no + 1, solution[1], solution[0])
        # print("Case #{}: {} {}\n".format(case_no + 1, solution[1], solution[0]))

    file_out = 'solutionC_2.out'
    with open(file_out, 'w') as f:
        f.write(output)


