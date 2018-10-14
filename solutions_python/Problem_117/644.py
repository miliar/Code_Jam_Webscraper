__author__ = 'saimanoj'


def find_yes_no():
    N, M = map(int, (raw_input()).split())
    desired_lawn = []
    row_max = []
    col_max = []
    for i in range(N):
        row = map(int, raw_input().split())
        desired_lawn.append(row)
        row_max.append(max(row))
        if i == 0:
            col_max = list(row)
        else:
            for j in range(M):
                if row[j] > col_max[j]:
                    col_max[j] = row[j]
    if N == 1 or M == 1:
        return 'YES'

    intermediate_lawn = [col_max[::]] * N

    final_lawn = []

    for i in range(N):
        final_lawn.append(
            [row_max[i] if intermediate_lawn[i][x] > row_max[i] else
             intermediate_lawn[i][x] for x in range(M)])

    if final_lawn == desired_lawn:
        return 'YES'
    else:
        return 'NO'


def main():
    T = int(raw_input())
    i = 1
    while i <= T:
        result_str = find_yes_no()
        print 'Case #' + str(i) + ': ' + result_str
        i += 1


if __name__ == '__main__':
    main()
