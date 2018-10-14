import sys


def indexes(val, l):
    return [i for i in range(len(l)) if val == l[i]]

def num_substrings(line, s):
    curr = {-1: 1}
    for c in line:
        for j in indexes(c, s):
            curr[j] = curr.get(j, 0) + curr.get(j - 1, 0)
    return curr.get(len(s) - 1, 0)

if __name__ == "__main__":
    f = file(sys.argv[1])
    g = file(sys.argv[2], 'w')
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        n = num_substrings(l, "welcome to code jam")
        g.write("Case #%s: " % (i + 1) + ("%4s" % n).replace(" ", "0")[-4:])
        g.write("\n")