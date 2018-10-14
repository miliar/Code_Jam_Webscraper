filename = "a.in"
outfilename = "output.txt"

def solve(f):
    r, c = map(int, f.readline().split())
    arr = []
    xs = []
    for i in range(r):
        row = f.readline().rstrip()
        for j in range(c):
            if row[j] in '<>^v':
                xs.append((i, j, row[j]))
        arr.append(row)

    output = 0

    for i in range(len(xs)):
        y, x, point = xs[i]
        ok = False
        present = False
        pointing = False
        for j in range(len(xs)):
            y1, x1, d = xs[j]
            if x == x1 and y == y1:
                continue
            if x == x1:
                present = True
                if y1 > y and point == 'v':
                    pointing = True
                    break
                if y1 < y and point == '^':
                    pointing = True
                    break
            if y == y1:
                present = True
                if x1 > x and point == '>':
                    pointing = True
                    break
                if x1 < x and point == '<':
                    pointing = True
                    break

        if not present:
            return "IMPOSSIBLE"
        if not pointing:
            output += 1



    return output

def out(s, o):
    print s
    o.write("{}\n".format(s))

def main():
    f = open(filename)
    o = open(outfilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1

if __name__ == "__main__":
    main()
