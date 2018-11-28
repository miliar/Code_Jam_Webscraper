#! /opt/local/bin/python
# -*- coding: utf8 -*-

def do_calc(points):
    size = len(points)
    count = 0

    for i in range(size):
        for j in range(i+1,size-1):
            for k in range(j+1, size):
                x = points[i][0] + points[j][0] + points[k][0]
                y = points[i][1] + points[j][1] + points[k][1]
                if ( ( x % 3 )  == 0 ) & ( ( y % 3 )== 0 ):
                    count += 1
    return count

def main():
    for case in range(input()):
        n, a, b, c, d, x0, y0, m = map(int,raw_input().split())
        points = []

        x = x0
        y = y0

        points.append([x,y])

        for i in range(1,n):
            x = ( a * x + b ) % m
            y = ( c * y + d ) % m
            points.append([x,y])

        value = do_calc(points)

        print 'Case #%d: %d' % ( case+1, value )

if __name__ == '__main__':
    main()
