def foo(cake):
    cake = [list(row) for row in cake]

    # fill up all rows that have initials
    for row in cake:
        found = False
        last_c = '.'
        for c in xrange(len(row)):
            if row[c] != '?':
                if not found:
                    found = True
                    for i in xrange(c):
                        row[i] = row[c]
                last_c = row[c]
            elif found:
                row[c] = last_c

    # fill up the rest
    found = False
    last_r = []
    for r in xrange(len(cake)):
        if cake[r][0] != '?':
            if not found:
                found = True
                for j in xrange(r):
                    cake[j] = cake[r]
            last_r = cake[r]
        elif found:
            cake[r] = last_r

    cake = [''.join(row) for row in cake]
    return '\n'.join(cake)

if __name__ == "__main__":
    fo = open("output", "w")
    with open("A-large.in") as f:
        text = [line.strip() for line in f.readlines()]
        i, case = 1, 1
        while i < len(text):
            args = text[i].split()
            r, c = int(args[0]), int(args[1])
            fo.write("Case #{0}:\n{1}\n".format(case, foo(text[i+1:i+r+1])))
            i += r + 1
            case += 1
    fo.close()