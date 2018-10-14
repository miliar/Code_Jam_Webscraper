# Google Code Jam
# Qualification Round
# Problem C - Bathroom Stalls
# Ing. S. Van Dessel
# 2017-04-08

FILE_NB = 1       # Switch between own (0), small 1 (1), small 2 (2) and large (3) test file

FILE_IN = ["test.in", "C-small-1-attempt0.in", "C-small-2-attempt0.in", "B-large.in"]
FILE_OUT = ["test.out", "C-small-1-attempt0.out", "C-small-2-attempt0.out", "B-large.out"]


def spacing(i, j, k):
    return j-i-1, k-j-1


def do_case(num_stalls, num_people):
    occupied = [0] + [num_stalls+1]

    for a in range(num_people):
        options = []
        for i, j in zip(range(len(occupied)-1), range(1, len(occupied))):
            l = occupied[i]
            r = occupied[j]

            idx = l + (r-l)//2
            opt = [idx]
            opt.extend(spacing(l, idx, r))
            options.append(opt)

            if (r-l) % 2 != 0:
                opt = [idx+1]
                opt.extend(spacing(l, idx+1, r))
                options.append(opt)

        min_space = max([min(x[1:]) for x in options])              # get best minimal spacing
        options = [x for x in options if min_space == min(x[1:])]   # only keep options with this min spacing

        max_space = max([max(x[1:]) for x in options])              # get best maximal spacing
        options = [x for x in options if max_space == max(x[1:])]   # only keep options with this max spacing

        choice = options[0]
        occupied.append(choice[0])
        occupied.sort()
    return max(choice[1:]), min(choice[1:])


def main():
    solution = ''
    with open(FILE_IN[FILE_NB], 'r') as f:
        f.readline()
        for i, line in enumerate(f):
            num_stalls, num_people = list(map(int,line.strip().split(' ')))
            stall_spacing = do_case(num_stalls, num_people)
            solution += "Case #{}: {} {}\n".format(i+1, stall_spacing[0], stall_spacing[1])

    solution = solution[:-1]                        # remove last new line
    with open(FILE_OUT[FILE_NB], 'w') as f:                  # write solution
        f.write(solution)


if __name__ == '__main__':
    main()
