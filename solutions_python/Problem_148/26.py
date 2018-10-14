def solve(N, X, S):
    """ solve the problem """

    #print(N, X, S)

    count = 0
    S.sort(reverse=True)

    while S:
        m = S.pop(0)
        count += 1 
        if len(S) > 0:
            found = None
            for i, s in enumerate(S):
                if s <= X - m:
                    found = i
                    break
            if found != None:
                S.pop(i)



    return count


def parse():
    """ parse input """

    N, X = map(int, input().split(' '))
    S = list(map(int, input().split(' ')))

    return N, X, S


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
