def solve(N, mine, others):
    """ solve the problem """

    mine.sort(reverse=True)
    others.sort(reverse=True)

    count1 = 0
    mine_index = 0
    others_index = 0
    while mine_index < N and others_index < N:
        if mine[mine_index] > others[others_index]: 
            count1 += 1         
            mine_index += 1
            others_index += 1
        else:
            others_index += 1

    count2 = 0
    mine_index = 0
    others_index = 0
    while mine_index < N and others_index < N:
        if mine[mine_index] < others[others_index]: 
            count2 += 1         
            mine_index += 1
            others_index += 1
        else:
            mine_index += 1

    return count1, N-count2


def parse():
    """ parse input """

    N = int(input())
    a = input().split()
    b = input().split()

    mine = list(map(float, a))
    others = list(map(float, b))

    return N, mine, others


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s %s' % (t, result[0], result[1]))


if __name__ == '__main__':

    main()
