
import math

case = "large"
input_file = "C-%s.in" % case
output_file = "C-%s.out" % case

fin = open(input_file)
fout = open(output_file, "w")

n = int(fin.readline().strip())

for z in range(1, n+1):
    f, R, t, r, g = [float(s) for s in fin.readline().strip().split()]
    
    area = math.pi * R ** 2
    hole = 0
    R -= t

    r += f
    g -= 2 * f
    R -= f

    in_circle = lambda x, y: x ** 2 + y ** 2 <= R ** 2
    squarell = lambda row, col: (r + col * (g + 2 * r), r + row * (g + 2 * r))

    if g > 0:
        row, col = 0, 0
        sqll = squarell(row, col)
        while in_circle(sqll[0]+g, sqll[1]+g):
            row += 1
            sqll = squarell(row, col)
        while row > 0 or in_circle(sqll[0], sqll[1]):
            if not in_circle(sqll[0], sqll[1]):
                row -= 1
                sqll = squarell(row, col)
            elif in_circle(sqll[0]+g, sqll[1]+g):
                row += 1
                hole += row * g ** 2
                col += 1
                sqll = squarell(row, col)
            else:
                ul = in_circle(sqll[0], sqll[1]+g)
                lr = in_circle(sqll[0]+g, sqll[1])
                if ul:
                    y1 = sqll[1]+g
                    x1 = (R ** 2 - y1 ** 2) ** 0.5
                else:
                    x1 = sqll[0]
                    y1 = (R ** 2 - x1 ** 2) ** 0.5
                if lr:
                    x2 = sqll[0]+g
                    y2 = (R ** 2 - x2 ** 2) ** 0.5
                else:
                    y2 = sqll[1]
                    x2 = (R ** 2 - y2 ** 2) ** 0.5
                if ul:
                    if lr:
                        hole += g ** 2 - (sqll[0]+g - x1) * (sqll[1]+g - y2) / 2
                    else:
                        hole += g * (x1 + x2 - 2 * sqll[0]) / 2
                else:
                    if lr:
                        hole += g * (y1 + y2 - 2 * sqll[1]) / 2
                    else:
                        hole += (y1 - sqll[1]) * (x2 - sqll[0]) / 2
                cross = abs(x1 * y2 - x2 * y1)
                a = math.asin(cross / (R ** 2))
                hole += (a * R ** 2 - cross) / 2
                if row > 0:
                    row -= 1
                else:
                    col += 1
                sqll = squarell(row, col)
        hole *= 4

    print >> fout, "Case #%d: %.6f" % (z, (area - hole) / area)

fin.close()
fout.close()
