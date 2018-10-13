__author__ = 'davidborsodi'

lol = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]


def solve(case):
    first = int(case[0])
    second = int(case[5])
    row1 = case[first]
    row2 = case[5 + second]
    ir1 = map(int, row1.split())
    ir2 = map(int, row2.split())
    # print ir1
    # print ir2
    guess = set(ir1).intersection(set(ir2))
    if len(guess) == 1:
        return list(guess)[0]
    elif len(guess) > 0:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'


if __name__ == '__main__':
    lines = [line.rstrip() for line in open('11in')]
    case = 1
    inputs = lol(lines[1:], 10)
    for i in inputs:
        # print i
        print 'Case #{c}: {res}'.format(c=case, res=solve(i))
        case += 1
