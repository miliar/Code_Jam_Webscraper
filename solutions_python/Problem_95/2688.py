import sys

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


def transpose(dict, line):
    pos = 0
    new_str = ""
    while pos < len(line):
        new_str = new_str + d[line[pos]]
        pos += 1

    return new_str

lines = sys.stdin.readlines()
i = 0
for line in lines:
    line = line.strip()
    if i == 0:
        i += 1
        continue

    print "Case #{0}: {1}".format(i, transpose(d, line))
    i += 1

