

def main():
    t = int(input())
    for case in range(1, t + 1):
        ac, aj = map(int, input().split())
        acs = sorted([tuple(map(int, input().split())) + ('c',) for _ in range(ac)])
        ajs = sorted([tuple(map(int, input().split())) + ('j',) for _ in range(aj)])
        un = acs + ajs

        if (ac == 1 or aj == 1) and ac + aj == 1:
            res = 2
        elif ac == 1 and aj == 1:
            res = 2
        elif ac == 2:
            b1 = acs[1][1] - acs[0][0] > 720
            b2 = 1440 - acs[1][0] + acs[0][1] > 720

            if b1 and b2:
                res = 4
            else:
                res = 2
        elif aj == 2:
            b1 = ajs[1][1] - ajs[0][0] > 720
            b2 = 1440 - ajs[1][0] + ajs[0][1] > 720

            if b1 and b2:
                res = 4
            else:
                res = 2
        print('Case #{}: {}'.format(case, res))


if __name__ == '__main__':
    main()
