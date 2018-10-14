__author__ = 'Via'

# file_in = open('example_input.txt', 'r')
# file_in = open('A-small-attempt0.in', 'r')
file_in = open('A-large.in', 'r')
file_out = open('output.txt', 'a')
line_idx = 0


def solve(problem):
    stand_up = 0
    invited = 0

    for sh_lvl in range(len(problem)):
        invite = sh_lvl - stand_up
        person = int(problem[sh_lvl])
        if invite > 0 and person > 0:
            invited += invite
            stand_up += invite
        stand_up += person

    return invited


for line in file_in:
    line_idx += 1
    if line_idx == 1:
        test_case = int(line)
        continue

    problem = list(line)
    pp = problem.pop()
    pp = problem.pop(0)
    while pp != ' ':
        pp = problem.pop(0)
    result = solve(problem)
    print 'Case #{}: {}'.format(line_idx - 1, result)
    file_out.writelines('Case #{}: {}\n'.format(line_idx - 1, result))

file_out.close()
print 'done'