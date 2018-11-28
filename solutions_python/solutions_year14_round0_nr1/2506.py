def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(cases):
        guess_1 = int(in_file.readline())
        reveal_1 = []
        for i in range(0, 4):
            reveal_1.append([int(x) for x in in_file.readline().split()])
        guess_2 = int(in_file.readline())
        reveal_2 = []
        for i in range(0, 4):
            reveal_2.append([int(x) for x in in_file.readline().split()])
        solution = solve(guess_1, reveal_1, guess_2, reveal_2)
        lines.append('Case #%s: %s\n' % (case + 1, solution))
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.writelines(lines)
    out_file.close()

def solve(guess_1, reveal_1, guess_2, reveal_2):
    possibilities_1 = reveal_1[guess_1 - 1]
    possibilities_2 = [x for x in possibilities_1 if x in reveal_2[guess_2 - 1]]
    if len(possibilities_2) < 1:
        return 'Volunteer cheated!'
    elif len(possibilities_2) < 2:
        return possibilities_2[0]
    else:
        return 'Bad magician!'

parse('A-small')
