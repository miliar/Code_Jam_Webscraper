"""
Problem 01 - Standing Ovation
"""
import sys


def ovation(n, audience_list):
    standing = 0
    friends = 0
    i = 0
    while i < n+1:
        if audience_list[i] != 0:
            if standing >= i:
                standing += audience_list[i]
                i += 1
            else:
                friends += 1
                standing = friends
                i = 0
        else:
            i += 1
    return friends


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        if filename != '-':
            f = open(filename)

    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        audience_list = []
        n, audience = line.split(" ")
        n = int(n)
        for j in range(n+1):
            audience_list.append(int(audience[j]))
        min_friends = ovation(n, audience_list)
        print("Case #{}: {}".format(i+1, min_friends))
