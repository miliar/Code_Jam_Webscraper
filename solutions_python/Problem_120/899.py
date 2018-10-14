# -*- coding: utf-8 -*-
import math

# 遅すぎる
INPUT = 'rA-small-attempt0.in'
OUTPUT = 'output-round1A-A-small.txt'

PAI = 1
REQUIRED = 1


def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def main():
    input = open(INPUT, 'r')

    caseno = 0
    data = []
    input.readline()    # 1行目は無視
    for line in input:
        count = 0
        ring = 0
        t_black = 0
        t_draw = 0
        line = line.replace('\n', '')
        data = line.split(' ')
        if len(data) == 2:
            r = int(data[0])
            t = int(data[1])

            # 最初の白
            area_white = r * r
            # 最初の黒
            area_black = (r+1) * (r+1) - area_white
            t_black = area_black
            ring += 1

            while True:
                area_black += 4
                t_black += area_black
                if t < t_black:
                    break

                ring += 1

        caseno += 1
        result(caseno, ring)

    input.close()


if __name__ == '__main__':
    main()
