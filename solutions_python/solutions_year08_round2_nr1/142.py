#! /usr/bin/env python

def calc(p):
    n = len(p)
    count = 0
    for i in range(n-2):
        x = p[i][0]
        y = p[i][1]
        for j in range(i+1,n-1):
            x2 = x + p[j][0]
            y2 = y + p[j][1]
            for k in range(j+1,n):
                x3 = x2 + p[k][0]
                y3 = y2 + p[k][1]
                if x3 % 3 == 0 and y3 % 3 == 0:
                    count += 1
    return count
def main():
    ifs = open("A-small-attempt2.in")
    ofs = open("out-a.txt", "w")
    num_cases = int(ifs.readline())
    for i in range(num_cases):
        n, A, B, C, D, x0, y0, M = map(int, ifs.readline().split())
        X, Y = x0, y0
        points = []
        points.append((X,Y))
        for j in range(n-1):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            points.append((X,Y))
        ofs.write("Case #%d: %d\n" % (i + 1, calc(points)))


if __name__ == "__main__":
    main()
