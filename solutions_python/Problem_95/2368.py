import sys

d = {'q': 'z', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}



T = sys.stdin.readline()

for i in range(1, int(T) + 1):
    s = sys.stdin.readline()
    s = s.strip()
    print "Case #%d: " % i,
    for c in s:
        if (c == ' '):
            sys.stdout.write(' ')
        else:
            sys.stdout.write(d[c])
    if i + 1 != int(T) + 1:
        print "\n"
