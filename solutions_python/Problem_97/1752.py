#http://code.google.com/codejam/contest/1460488/dashboard#s=p2

input = open('C-small.in', 'r')
output = open('C-output.txt', 'w')
cases = int(input.readline())
origin = [line.rstrip('\n') for line in input]

numbers = []

for line in origin:
    for char in line:
        if char == ' ':
            dex = line.index(char)
            numbers.append([int(line[:dex])] + [int(line[dex+1:])])


recycle = []

for pair in numbers:
    pairs = []
    for n in xrange(pair[0], pair[1]+1):
        for m in xrange(n, pair[1]+1):
            n = str(n)
            m = str(m)
            if len(n) == 2 and n < m:
                if n[1] == m[0] and n[0] == m[1] and int(m) > 10:
                    pairs.append(2)
            elif len(n) == 3 and n < m:
                if n[1:] == m[:2] and n[0] == m[2] and int(m) > 100:
                    pairs.append(3)
                elif n[2] == m[0] and n[:2] == m[1:] and int(m) > 100:
                    pairs.append(3)
            elif len(n) == 4 and n < m:
                if n[1:] == m[:3] and n[0] == m[3] and int(m) > 1000:
                    pairs.append(3)
                elif n[2:] == m[:2] and n[:2] == m[2:] and int(m) > 1000:
                    pairs.append(3)
                elif n[3] == m[0] and n[:3] == m[1:] and int(m) > 1000:
                    pairs.append(3)
    recycle.append(len(pairs))


print recycle

for x in xrange(cases):
    string = 'Case #%d: %s\n' % (x+1, recycle[x])
    output.write(string)