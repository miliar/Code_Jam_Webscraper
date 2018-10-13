#!/usr/bin/python
filename = "/Users/oliversu/Downloads/A-large.in.txt"
for (n, line) in enumerate(list(open(filename, 'rt'))[1:]):
    done = 0
    need = 0
    items = line.strip().split(" ");
    for (i, d) in enumerate(items[1]):
        d = int(d)
        if i == 0:
            if d == 0:
                done += 1
                need += 1
            else:
                done += d
        else:
            if done < i and d > 0:
                need += (i - done)
                done += (i - done) + d
            else:
                done += d
    print "Case #%d: %d" % (n+1, need)
