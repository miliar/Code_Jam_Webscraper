def solve(N):
    """ solve the problem """

    for i in range(len(N)-1, 0, -1):
        if N[i-1] > N[i]:
            N = str(int(N[:i])-1) + '9'*(len(N)-i)

    N = N.lstrip('0')

    return N


def parse():
    """ parse input """

    N = input()

    return N


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
