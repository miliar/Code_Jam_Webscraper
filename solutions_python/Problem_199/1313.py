import sys
import math

def flip(s, i, k):
    """flips the first three bits of s from index i to index i + k"""
    s = list(s)
    for j in range(k):
        if s[i + j] == "-":
            s[i + j] = "+"
        else:
            s[i + j] = "-"
    return "".join(s)

def compute_min_flips(s, k):
    k = int(k)
    l = list(s)
    count = 0
    for i in range(len(l) - k + 1):
        char = l[i]
        if char == "-":
            s = flip(s, i, k)
            l = list(s)
            count += 1

    if "-" in s:
        return "IMPOSSIBLE"
    else:
        return count

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        case = 0
        for line in f:
            if case == 0:
                case += 1
                continue
            args = line.split(" ")
            print "Case #%s: %s" % (case, compute_min_flips(args[0], args[1]))
            case += 1

