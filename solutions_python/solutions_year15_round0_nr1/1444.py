import sys

__author__ = 'xl'

if __name__ == "__main__":
    fp = open("A.in")
    sys.stdout = open("A.out", "w")
    # fp = sys.stdin

    T = int(fp.readline())
    for t in range(T):
        input_line = fp.readline()
        S = int(input_line.split()[0])
        ans = 0
        cum_sum = 0
        for i, c in enumerate(input_line.split()[1]):
            if cum_sum < i and int(c) > 0:
                ans += i - cum_sum
                cum_sum = i

            cum_sum += int(c)

        print "Case #%s: %s" % (t + 1, ans)


