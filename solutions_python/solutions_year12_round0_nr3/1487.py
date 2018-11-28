from collections import deque

lines = file("C-small-attempt1.in").read().split('\n')

x = 1
out = ""
for line in lines[1:-1]:
    y=0
    a, b = tuple([int(n) for n in line.split()])
    numbers = [(str(n)) for n in range(a,b+1)]
    d = {}
    for number in numbers:
        sort = tuple(sorted(number))
        if  sort in d:
            d[sort].append(number)
        else:
            d[sort] = [number]

    for group in d.values():
        if len(group) < 2:
            continue
        for number in group:
            rest = group[:]
            rest.remove(number)
            y += [n in number*2 for n in rest].count(True)

    y = y/2

    out += "Case #%s: %s\n" % (x,y)
    x += 1

print out
open("output", "w").write(out[:-1])
