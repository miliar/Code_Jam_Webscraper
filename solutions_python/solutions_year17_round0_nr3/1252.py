# Problem C


def get_max_square(k):
    square = 1
    while True:
        if square > k:
            return square/2
        elif square == k:
            return square
        else:
            square *= 2


def solve(n, k):

    # 0, 0
    # 1, 0
    # 1, 1
    # n, n-1
    # n, n

    remain = n
    remain -= k
    square_max = get_max_square(k)
    remain -= square_max

    if remain < 0:
        return 0, 0

    r = int(remain / (square_max * 2))
    m = remain - (r * square_max * 2)

    if m < square_max:
        return r + 1, r + 0
    else:
        return r + 1, r + 1


def main():
    #inputFile = "C-small-1-attempt0.in"
    inputFile = "C-small-2-attempt0.in"
    #inputFile = "C-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    #false_msg = "IMPOSSIBLE"

    for case in range(test_case):

        n, k = [int(x) for x in inpf.readline().strip().split(' ')]
        ma, mi = solve(n, k)

        result = 'Case #{}: {} {}\n'.format(case + 1, ma, mi)

        print(result, end='')
        outf.write(result)
    inpf.close()
    outf.close()



def test_proc(cases):
    for case in cases:
        n = case[0]
        k = case[1]
        emax = case[2]
        emin = case[3]

        amax, amin = solve(n, k)
        if amax != emax or amin != emin:
            print(n, k, emax, emin, 'expected but ', amax, amin)

def test():
    test_cases = list()


    test_proc(test_cases)


if __name__ == "__main__":
    main()
    #test()
    # 500 255
    #ma, mi = solve(500, 255)
    # print(ma, mi)