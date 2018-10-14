#!/usr/bin/env python
# works with both python 2 & 3
import fileinput


def make_answer(case, result):
    if isinstance(result, int):
        answ = str(result)
    elif result is None:
        answ = "Volunteer cheated!"
    else:
        answ = "Bad magician!"
    return "Case #%s: %s" % (case, answ)


def solve_round(answ1, disp1, answ2, disp2):
    # disps are tuples of sets, answ are ints
    result = disp1[answ1 - 1] & disp2[answ2 - 1]
    if not result:
        return None
    elif len(result) == 1:
        return result.pop()
    else:
        return result


def get_input(lines):
    nextline = lambda: next(lines)

    cases = int(nextline())
    for _ in range(cases):
        answ1 = int(nextline())
        disp1 = []
        for _ in range(4):
            disp1.append(set(map(int, nextline().split())))
        disp1 = tuple(disp1)
        answ2 = int(nextline())
        disp2 = []
        for _ in range(4):
            disp2.append(set(map(int, nextline().split())))
        disp2 = tuple(disp2)
        yield (answ1, disp1, answ2, disp2)


def main():
    for i, game in enumerate(get_input(fileinput.input()), 1):
        print(make_answer(i, solve_round(*game)))

if __name__ == '__main__':
    main()
