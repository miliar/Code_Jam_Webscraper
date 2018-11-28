#!/usr/bin/env python3

def play_deceitful_war(naomi, ken):
    naomi = list(naomi)
    ken   = list(ken)

    score_naomi = 0

    while len(naomi) > 0:
        if naomi[0] > ken[-1]:
            return score_naomi + len(ken)

        elif naomi[0] > ken[0]:
            # Bluff!
            naomi.pop(0)
            ken.pop(0)
            score_naomi += 1

        else:
            naomi.pop(0)
            ken.pop(-1)

    return score_naomi


def play_war(naomi, ken):
    naomi = list(naomi)
    ken   = list(ken)

    score_naomi = 0
    ki = 0

    for n in naomi:
        if n > ken[-1]:
            score_naomi += 1
            ki = max(ki - 1, 0)
            ken.pop(0)
        else:
            while ken[ki] < n:
                ki += 1
            ken.pop(ki)

    return score_naomi


def solve_testcase(testcase_number):
    num_blocks = int(input())
    naomi = sorted(float(i) for i in input().split())
    ken   = sorted(float(i) for i in input().split())

    print('Case #{0}: {1} {2}'.format(testcase_number,
        play_deceitful_war(naomi, ken), play_war(naomi, ken)))


def main():
    testcases = int(input())
    for t in range(testcases):
        solve_testcase(t + 1)


if __name__ == '__main__':
    main()
