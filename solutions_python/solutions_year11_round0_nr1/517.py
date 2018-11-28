import fileinput

def read_cases(file):
    N = int(file.readline())
    for caseno in range(1, N+1):
        line = file.readline().split()
        M  = int(line[0])
        assert len(line) == M*2 + 1
        yield caseno, [(x, int(y)) for x,y in zip(line[1::2], line[2::2])]

def solve_case(problem):
    time = {'B':0, 'O':0}
    pos  = {'B':1, 'O':1}
    now = 0

    for color, where in problem:
        prev_time = time[color]
        prev_pos  = pos[color]
        next_time = prev_time + abs(where-prev_pos) + 1
        if now >= next_time:
            next_time = now+1
        time[color] = now = next_time
        pos[color] = where
    return now

def _test():
    assert solve_case([('O', 2)]) == 2
    assert solve_case([('O', 2), ('B', 2)]) == 3

def main():
    for no, case in read_cases(fileinput.input()):
        print "Case #%d:" % no, solve_case(case)

if __name__ == '__main__':
    #_test()
    main()
