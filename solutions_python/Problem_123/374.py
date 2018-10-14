def doInsert(A, item, N):
    times = 0
    while A <= item and times <= N:
        A += A - 1
        times += 1
    A += item
    return times, A


def main():
    fin = open("input", "r")
    fout_tmp = open("tmp", "w")
    fout = open("output", "w")
    T = int(fin.readline())
    print >> fout_tmp, T
    for testcase in range(1, T + 1):
        A, N = [int(item) for item in fin.readline().split()]
        print >> fout_tmp, A, N
        motes = [int(item) for item in fin.readline().split()]
        motes = sorted(motes)
        print >> fout_tmp, motes
        result = 0
        for i in range(N):
            if A <= motes[i]:
                tmp_result, tmp_A = doInsert(A, motes[i], N)
                if result + tmp_result >= N or tmp_result >= N - i:
                    result = min(N, N + result - i)
                    break
                else:
                    result += tmp_result
                    A = tmp_A
            else:
                A = A + motes[i]
        print >> fout, "Case #%d: %d" % (testcase, result)


if __name__ == '__main__':
    main()
