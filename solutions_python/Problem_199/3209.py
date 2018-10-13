import sys


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        pancake, k = raw_input("").split()
        k = int(k)
        res = 0
        res = dfs(pancake, 0, 0, k)
        if(res == sys.maxint):
            res = 'IMPOSSIBLE'
        print "Case #{}: {}".format(i, res)


def dfs(pancake, index, depth, k):
    if(pancake == '+' * len(pancake)):
        return depth
    if(index == len(pancake) or index + k - 1 == len(pancake)):
        return sys.maxint
    res = sys.maxint
    for i in range(index, len(pancake) - k + 1):
        if(pancake[i] != '-'):
            continue
        new_pancake = flip(pancake, i, i + k - 1)
        res = min(res, dfs(new_pancake, i + 1, depth + 1, k))
    return res


def flip(s, start, end):
    new = s[:start]
    for i in range(start, end + 1):
        if s[i] == '-':
            new += '+'
        else:
            new += '-'
    new += s[end + 1:]
    return new
if __name__ == '__main__':
    main()
