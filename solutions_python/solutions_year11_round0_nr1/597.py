import csv
import os
import sys

ORANGE = 0
BLUE = 1

def solve(N, buttons):
    x_robot = [1, 1]
    t = 0
    s = 0

    prev_color = None
    for _color, x in buttons:
        if _color == 'O':
            color = ORANGE
        else:
            color = BLUE

        x_press = x_robot[color]

        if prev_color != color \
                and prev_color is not None:
            dt = max(0, abs(x - x_press) - s) + 1
            s = dt
        else:
            dt = abs(x - x_press) + 1
            s += dt

        t += dt
        x_robot[color] = x
        prev_color = color
    return t

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        r = reader.next()
        N = int(r[0])

        buttons = []
        for i in range(N):
            buttons.append((r[2 * i + 1], int(r[2 * i + 2])))

        answer = solve(N, buttons)
        dst.write("Case #%d: %s\n" % (t + 1, answer))

    assert src.read() == ""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python solve.py input output"
        raise SystemExit

    src_path = os.path.abspath(sys.argv[1])
    src = open(src_path, "r")

    
    dst_path = os.path.abspath(sys.argv[2])
    if os.path.exists(dst_path):
        print "already exists: %s" % dst_path
        raise SystemExit
    dst = open(dst_path, "w")

    try:
        main(src, dst)
    finally:
        src.close()
        dst.close()
