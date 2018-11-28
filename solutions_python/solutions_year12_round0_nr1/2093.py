import sys
mapping = {' ':' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd',
 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z',
'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
'x': 'm', 'z': 'q'}

n = input()

for i in xrange(n):
    s = []
    line = raw_input()
    for j in xrange(len(line)):
        s.append(mapping[line[j]])
    sys.stdout.write("Case #"+str(i+1)+": "+''.join(k for k in s))
    print
