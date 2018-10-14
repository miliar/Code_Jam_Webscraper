import sys

num_lines_per_case = 10
lines = sys.stdin.readlines()
num_cases = int(lines[0])

for i in xrange(1, num_cases + 1):
    first_row = (i - 1) * num_lines_per_case + 1
    second_row = first_row + num_lines_per_case / 2
    first_set = set([int(x) for x in lines[first_row + int(lines[first_row])].split(' ')])
    second_set = set([int(x) for x in lines[second_row + int(lines[second_row])].split(' ')])
    matches_set = first_set & second_set

    sys.stdout.write("Case #{}: ".format(i))
    if len(matches_set) == 1:
        sys.stdout.write("{}\n".format(int(list(matches_set)[0])))
    elif len(matches_set) >= 1:
        sys.stdout.write("Bad magician!\n")
    else:
        sys.stdout.write("Volunteer cheated!\n")
