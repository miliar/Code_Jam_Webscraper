from sys import stdin, stdout
trials = stdin.readline()
for i, line in enumerate(stdin.readlines()):
    n,k = map(int, line.split())
    states = 2 ** n
    stdout.write('Case #%s: %s\n' % (i+1, 'ON' if k % states == states - 1 else 'OFF'))