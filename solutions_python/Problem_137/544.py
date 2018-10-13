import cPickle as pickle


def main():
    d = pickle.load(open('c.pickle', 'rb'))
    num_of_tests = int(raw_input())
    for test_i in range(num_of_tests):
        n, m, k = map(int, raw_input().split())
        ans = d['%s-%s-%s' % (n, m, k)]
        if k == n * m - 1:
            ans = 'c' + '*' * (m - 1) + '\n'
            for i in range(n - 1):
                ans += '*' * m + '\n'
        print "Case #%d:" % (test_i + 1)
        if ans[-1] == '\n':
            ans = ans[:-1]
        print ans


if __name__ == "__main__":
    main()
