def run_case(ans1, matrix1, ans2, matrix2):
    res = matrix1[ans1-1].intersection(matrix2[ans2-1])
    if len(res)>1:
        return 'Bad magician!'
    if len(res) == 0:
        return 'Volunteer cheated!'
    return res.pop()


def __parse_stdin():
    n = int(raw_input())
    cases = []
    for i in xrange(n):
        ans1 = int(raw_input())
        matrix1 = __read_matrix()
        ans2 = int(raw_input())
        matrix2 = __read_matrix()
        cases.append((ans1,matrix1,ans2,matrix2))
    return cases


def __read_matrix():
    ret = []
    for j in xrange(4):
        ret.append(set([int(x) for x in raw_input().split(' ')]))
    return ret


def main():
    cases = __parse_stdin()
    i = 1
    for a1,m1,a2,m2 in cases:
        print 'Case #%d:' % i,
        print run_case(a1,m1,a2,m2)
        i += 1


if __name__ == '__main__':
    main()
