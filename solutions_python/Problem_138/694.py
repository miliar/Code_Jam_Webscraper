#! /usr/bin/env python3
# Deceitful War


def play_deceitful_war(n_woods, naomi, ken):
    naomi.sort()
    ken.sort()
    while len(naomi):
        if all(a > b for a, b in zip(naomi, ken)):
            break
        naomi = naomi[1:]
        ken.pop()
    return len(naomi)


def play_war(n_woods, naomi, ken):
    naomi.sort()
    ken.sort()
    win = 0
    for n in naomi:
        try:
            found = next(i for i in ken if i > n)
            ken.remove(found)
        except StopIteration:
            win += 1
    return win


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        n_woods = int(input())
        naomi = [float(i) for i in input().split()]
        ken = [float(i) for i in input().split()]
        deceitful_war = play_deceitful_war(n_woods, naomi[:], ken[:])
        war = play_war(n_woods, naomi[:], ken[:])

        print('Case #{}: {} {}'.format(i, deceitful_war, war))


if __name__ == '__main__':
    main()
