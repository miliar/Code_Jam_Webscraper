def solve(case, count=0):
    stand_up = int(case[0])
    idx = 0
    for people in case[1:]:
        idx += 1
        if stand_up >= idx:
            stand_up += int(people)
        else:
            case = str(int(case[0]) + 1) + case[1:]
            return solve(case, count + 1)

    if stand_up >= len(case):
        return count


def parse_input():
    return list(map(lambda x: x.split(' ')[1:][0].replace('\n', ''), open('input.txt', 'r').readlines()[1:]))

if __name__ == "__main__":
    input = parse_input()
    case = 1
    with open("result.txt", 'w') as result:
        for i in input:
            result.write("Case #%d: %d\n" % (case, solve(i)))
            case += 1