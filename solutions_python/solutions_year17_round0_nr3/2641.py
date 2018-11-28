import sys

def adjust_left_counts(x, stalls):
    l = len(stalls)
    count = 0
    i = x + 1
    while i < l:
        if stalls[i] == "X":
            return
        stalls[i] = (count, stalls[i][1])
        count += 1
        i += 1

def adjust_right_counts(x, stalls):
    count = 0
    i = x - 1
    while i >= 0:
        if stalls[i] == "X":
            return
        stalls[i] = (stalls[i][0], count)
        count += 1
        i -= 1

def place_person(stalls):
    max_min = None
    max_max = None
    best_pos = None
    best_stall = None

    for i, stall in enumerate(stalls):
        if stall == "X":
            continue

        if (max_min is None and max_max is None) or min(stall) > max_min or (min(stall) == max_min and max(stall) > max_max):
            max_min = min(stall)
            max_max = max(stall)
            best_pos = i
            best_stall = (stall[0], stall[1])

    stalls[best_pos] = "X"
    adjust_left_counts(best_pos, stalls)
    adjust_right_counts(best_pos, stalls)

    return best_stall

def solve(num_stalls, num_people):
    num_stalls = int(num_stalls)
    num_people = int(num_people)

    if num_stalls == 1 or num_stalls == num_people:
        return "0 0"
    #if num_people == num_stalls - 1:
        #return "1 0"

    stalls = ["X"] + [(0,0) for i in xrange(num_stalls)] + ["X"]
    adjust_left_counts(0, stalls)
    adjust_right_counts(num_stalls + 1, stalls)
    
    chosen_stall = None
    for p in xrange(num_people):
        chosen_stall = place_person(stalls)

    #print stalls
    #print chosen_stall
    return "{} {}".format(max(chosen_stall), min(chosen_stall))

def get_input(filename):
    with file(filename, "r") as infile:
        lines = infile.readlines()[1:]
        return [line.strip().split(" ") for line in lines]

def write_out(input_lines):
    with file("out.txt", "w") as outfile:
        for i, line in enumerate(input_lines):
            outfile.write("Case #{}: {}\n".format(i+1, solve(*line)))

if __name__ == '__main__':
    write_out(get_input(sys.argv[-1]))
    #print solve(500, 499)
