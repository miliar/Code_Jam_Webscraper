googlerese = "ynficwlbkuomxsevzpdrjgthaq"
alpha =      "abcdefghijklmnopqrstuvwxyz"

f = open("input.txt")

a = 0

for line in f:
    if a == 0:
        a += 1
        continue
    new = ""
    old = line
    for char in old:
        count = 0
        if char == " ":
            new += char
            continue
        for c in googlerese:
            if c == char:
                new += alpha[count]
            count += 1
    print "Case #" + str(a) + ": " + new
    a += 1

