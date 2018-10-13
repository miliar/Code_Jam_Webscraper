def solve(C, F, X):
    """ solve the problem """

    seconds = 0.0
    rate = 2.0

    buildings = 0

    while True:
        seconds += C / rate
        remains = X - C

        # s1: dont buy new building
        strategy1 = remains / rate

        # s2: buy new building
        strategy2 = ( remains + C ) / ( rate + F )

        if strategy1 <= strategy2:
            seconds += strategy1
            return seconds

        # buy new building
        rate += F


def parse():
    """ parse input """

    C, F, X = map(float, input().split())

    return C, F, X


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %.7f' % (t, result))


if __name__ == '__main__':

    main()
