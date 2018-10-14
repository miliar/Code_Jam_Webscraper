import sys


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        k = int(raw_input(""))
        res = helper(k)
        print "Case #{}: {}".format(num, res)


def helper(k):
    if(k % 10 != 0 and str(k) == ''.join(sorted(str(k)))):
        return k
    a = list(str(k))
    for i in range(len(a)):
        if(a[i] > a[i + 1]):
            a[i] = str(int(a[i]) - 1)
            a[i+1:] = '9' * (len(a) - i - 1)
            return helper(int("".join(a)))
    return int("".join(a))
if __name__ == '__main__':
    main()
