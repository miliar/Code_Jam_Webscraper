>>> file(r'c:\var\tmp\out.txt', 'w').write(''.join(['Case #%d: %s\n' % (i + 1, '
'.join([q.get(c, ' ') for c in line])) for (i, line) in enumerate([line.strip()
for line in file(r'c:\var\tmp\in.txt').readlines() if line][1:])]))
