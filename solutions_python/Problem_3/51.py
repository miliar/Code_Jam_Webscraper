#! /usr/bin/env python

from math import pi, sin, asin, sqrt

def calcSingleArea(r, g, x_left, x_right, y_max_left, y_max_right, y_bottom):
    y_top = y_bottom + g
    if y_top < y_max_right:
        return g * (x_right - x_left)
    elif y_top < y_max_left and y_bottom < y_max_right:
        x_top = sqrt(r**2 - y_top**2)
        return g * (x_top - x_left) + integ(r, x_top, x_right) - y_bottom * (x_right - x_top)
    elif y_top < y_max_left and y_bottom > y_max_right:
        x_bottom = sqrt(r**2 - y_bottom**2)
        x_top = sqrt(r**2 - y_top**2)
        return g * (x_top - x_left) + integ(r, x_top, x_bottom) - y_bottom * (x_bottom - x_top)
    elif y_top > y_max_left and y_bottom < y_max_right:
        return integ(r, x_left, x_right) - y_bottom * (x_right - x_left)
    else:
        x_bottom = sqrt(r**2 - y_bottom**2)
        return integ(r, x_left, x_bottom) - y_bottom * (x_bottom - x_left)
        

def integ(r, x_left, x_right):
    tleft = asin(x_left / r)
    tright = asin(x_right / r)
    return r**2 / 2. * (tright - tleft + (sin(2. * tright) - sin(2. * tleft)) / 2.)
    
def calc(R, r, w, g):
    total_area = pi * R**2 / 4.
    void_area = 0.
    x_left = w / 2.
    while x_left < r:
        y_bottom = w / 2.
        x_right = min(x_left + g, r)
        y_max_left = sqrt(r**2 - x_left**2)
        y_max_right = sqrt(r**2 - x_right**2)
        while y_bottom < y_max_left:
            area = calcSingleArea(r, g, x_left, x_right, y_max_left, y_max_right, y_bottom)
            void_area += area
            y_bottom += g + w
        x_left += g + w
    return 1. - (void_area / total_area)
    

def main():
    ifs = open("C-small-attempt0.in")
    ofs = open("out-c.txt", "w")
    num_cases = int(ifs.readline())
    for i in range(num_cases):
        f, R, t, r, g = map(float, ifs.readline().split())
        ofs.write("Case #%d: %.6f\n" % (i + 1, calc(R, R - t - f, 2 * (r + f), g - 2 * f)))


if __name__ == "__main__":
    main()
