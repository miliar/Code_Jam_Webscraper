def solve(R, C, arr):
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '?':
                if c > 0:
                    arr[r][c] = arr[r][c-1]
        for c in range(C):
            if arr[r][C-1-c] == '?':
                if c > 0:
                    arr[r][C-1-c] = arr[r][C-c]
    for r in range(R):
        if arr[r].count('?') == C:
            if r > 0:
                arr[r] = arr[r-1]
    for r in range(R):
        if arr[R-1-r].count('?') == C:
            if r > 0:
                arr[R-1-r] = arr[R-r]
    return arr


def main():
    # f_in = open('A-small-test.in')
    # f_in = open('A-small-attempt0.in')
    f_in = open('A-large.in')
    # f_out = open('A-small.out', 'w')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        R, C = [int(i) for i in f_in.readline().split()]
        arr = []
        for i in range(R):
            arr.append(list(f_in.readline().strip()))
        s = solve(R, C, arr)
        f_out.write("Case #{}:\n".format(t+1))
        for a in s:
            f_out.write("{}\n".format(''.join(a)))
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
