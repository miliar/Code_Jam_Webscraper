def main():
    num_of_tests = int(raw_input())
    a = [0 for i in range(4)]
    for test_i in range(num_of_tests):
        row1 = int(raw_input())
        for i in range(4):
            a[i] = map(int, raw_input().split())
        x = a[row1 - 1][:]
        row2 = int(raw_input())
        for i in range(4):
            a[i] = map(int, raw_input().split())
        y = a[row2 - 1][:]
        r = list(set(x) & set(y))
        ans = None
        if len(r) == 1:
            ans = r[0]
        elif len(r) == 0:
            ans = 'Volunteer cheated!'
        else:
            ans = 'Bad magician!'
        print "Case #%d: %s" % (test_i + 1, ans)


if __name__ == "__main__":
    main()
