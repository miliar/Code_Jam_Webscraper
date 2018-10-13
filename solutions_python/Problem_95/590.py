import sys
mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
n = sys.stdin.readline()
for i, line in enumerate(sys.stdin):
    value = ""
    line = line.split("\n")[0]
    for c in line:
        if c in mapping:
            value += mapping[c]
        else:
            value += c
    print "Case #%d: %s" % (i+1, value)
    