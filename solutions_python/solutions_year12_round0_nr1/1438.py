map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q'}
with open('in.txt') as f:
    lines = f.readlines()
    for line, i in zip(lines, range(len(lines))):
        print "Case #" + str(i + 1) + ': ' + ''.join((map[c] if c in map else c for c in line.strip()))