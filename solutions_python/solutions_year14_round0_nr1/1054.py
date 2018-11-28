bad_magician = "Bad Magician!"
volunteer_cheated = "Volunteer cheated!"

def solve(input):
    A = int(input.readline())
    arrangement = []
    for x in xrange(4):
        arrangement.append(input.readline())
    A_choice = set(arrangement[A-1].split())
    B = int(input.readline())
    arrangement = []
    for x in xrange(4):
        arrangement.append(input.readline())
    B_choice = set(arrangement[B-1].split())
    solution = A_choice.intersection(B_choice)
    if len(solution) > 1:
        return bad_magician
    if len(solution) == 0:
        return volunteer_cheated
    return solution.pop()

test_answer = {
    1: "7",
    2: bad_magician,
    3: volunteer_cheated
}

if __name__ == '__main__':
    import sys
    test = False
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = 'test.txt'
        test = True
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    with open(file_name) as f:
        T = int(f.readline())
        for i in range(1, T + 1):
            answer = solve(f)
            if test:
                assert answer == test_answer[i]
            else:
                print "Case #%d: %s" % (i, answer)
