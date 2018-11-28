import itertools

score_total = {0: [0, None], 1: [1, None], 2: [1, 2], 3: [1, 2], 4: [2, 2], 5: [2, 3], 6: [2, 3], 7: [3, 3], 8: [3, 4], 9: [3, 4], 10: [4, 4], 11: [4, 5], 12: [4, 5], 13: [5, 5], 14: [5, 6], 15: [5, 6], 16: [6, 6], 17: [6, 7], 18: [6, 7], 19: [7, 7], 20: [7, 8], 21: [7, 8], 22: [8, 8], 23: [8, 9], 24: [8, 9], 25: [9, 9], 26: [9, 10], 27: [9, 10], 28: [10, 10], 29: [10, None], 30: [10, None]}
invalids = {0, 1, 29, 30}

def get_max(torig, s, p):
    max_value = 0
    chosen_lists = itertools.permutations(range(len(torig)), s)
    for chosen_list in chosen_lists:
        sum_value = 0
        highests = []

        chosen_totals = set([torig[x] for x in chosen_list])
        if len(chosen_totals.intersection(invalids)) > 0:
            continue

        for idx in range(len(torig)):
            if idx in chosen_list:
                highests.append(score_total[torig[idx]][1])
            else:
                highests.append(score_total[torig[idx]][0])
        sum_value = len([h for h in highests if h >= p])

        if sum_value > max_value:
            max_value = sum_value

    return max_value

in_file_str = "B-small-attempt0.in"
out_file_str = "B.out"

with open(in_file_str) as infile:
    outfile = open(out_file_str, "w")
    num_cases = int(infile.readline())
    for q in range(num_cases):
        line_values = [int(x) for x in infile.readline().split()]

        N = line_values[0]
        S = line_values[1]
        p = line_values[2]
        torig = line_values[3:]

        out_str = "Case #%d: %d\n" % (q + 1, get_max(torig, S, p))
        outfile.write(out_str)
