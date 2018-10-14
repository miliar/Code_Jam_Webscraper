PATH_INPUT = 'C-small-attempt0.in'
PATH_OUTPUT = 'C-code.out'

import math

def pointInCircle(x, y, radius):
    return x * x + y * y <= radius * radius

def calcRectAreaBounded(iR, x1, y1, x2, y2):
    # y
    # ^
    # |
    # | C D
    # | A B
    # +-------> x
    # A = (x1, y1)
    # D = (x2, y2)
    aInCircle = pointInCircle(x1, y1, iR)
    bInCircle = pointInCircle(x2, y1, iR)
    cInCircle = pointInCircle(x1, y2, iR)
    dInCircle = pointInCircle(x2, y2, iR)

    area = 0

    if aInCircle:

        if bInCircle:
            if cInCircle:
                if dInCircle:
                    return (x2 - x1) * (y2 - y1)
                else:
                    area += (math.sqrt(iR * iR - y2 * y2) - x1) * (y2 - y1)
                    x1 = math.sqrt(iR * iR - y2 * y2)

        else:
            if cInCircle:
                x1, x2, y1, y2 = y1, y2, x1, x2

            else:
                x2 = math.sqrt(iR * iR - y1 * y1)

    else:
        return 0.

    # Integral for calculating area under a circle bounded below by a line y = y1
    ##if iR * iR == x2 * 2:
    ##    return 0.
    area += ((math.asin(x2 / iR) - math.asin(x1 / iR)) * iR * iR \
             + x2 * math.sqrt(iR * iR - x2 * x2) \
             - x1 * math.sqrt(iR * iR - x1 * x1)) / 2. - y1 * (x2 - x1)

    return area

def calculate(f, R, t, r, g):
    # Get total area
    totalArea = math.pi * R**2.

    # Get grid area
    quarterSpaces = 0.
    for i in range(int((R - t - f) / (g + 2 * r)) + 1):
        for j in range(int((R - t - f) / (g + 2 * r)) + 1):
            #print (R - t - f, i * (g + 2 * r) + r + f, j * (g + 2 * r) + r + f, i * (g + 2 * r) + g + r - f, j * (g + 2 * r) + g + r - f)
            quarterSpaces += calcRectAreaBounded(R - t - f, i * (g + 2 * r) + r + f, j * (g + 2 * r) + r + f, i * (g + 2 * r) + g + r - f, j * (g + 2 * r) + g + r - f)

    return 1 - 4. * quarterSpaces / totalArea

def main():
    # Load input
    inp = open(PATH_INPUT)
    inpL = inp.readlines()
    inp.close()
    del inp

    # Prepare output
    out = open(PATH_OUTPUT, 'w')
    out.truncate(0)

    mode = 0

    for line in inpL:
        line = line.strip()

        # Load num of cases
        if mode == 0:
            N = int(line)
            case = 0
            mode = 1

        # Load vals & do calculation
        elif mode == 1:
            case += 1
            f, R, t, r, g = line.split()
            f, R, t, r, g = float(f), float(R), float(t), float(r), float(g)
            p = calculate(f, R, t, r, g)
            print 'Case #%i: %.6f' % (case, p)
            out.write('Case #%i: %.6f\n' % (case, p))

            if case == N:
                break

    out.close()

main()
