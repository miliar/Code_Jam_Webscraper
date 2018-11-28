# Task C - Fly Swatter
# Written in Python

testing = False

from math import *

def curve(val1, val2, val3, rad):
    area = (val1-val2)*val3
    val1 = asin(val1/rad)
    val2 = asin(val2/rad)
    area += rad**2*((val2-val1)/2+(sin(2*val2)-sin(2*val1))/4)
    return area

def probability(data):
    data = [float(num) for num in data]
    fly_rad, racket_rad, racket_edge, string_rad, string_gap = data
    area = pi*racket_rad**2/4
    overlap_area = 0
    overlap_width = string_gap-2*fly_rad
    racket_inner = racket_rad-racket_edge-fly_rad
    overlap_gap = 2*string_rad+string_gap
    if overlap_width > 0:
        start_pos = string_rad+fly_rad
        left = start_pos
        while left < racket_inner:
            right = left+overlap_width
            if right > racket_inner:
                right = racket_inner
            left_height = sqrt(racket_inner**2-left**2)
            right_height = sqrt(racket_inner**2-right**2)
            bottom = start_pos
            while bottom < left_height:
                top = bottom+overlap_width
                if top > left_height:
                    top = left_height
                if top < right_height:
                    overlap_area += (right-left)*(top-bottom)
                else:
                    val3 = left
                    val2 = top
                    val1 = bottom
                    if bottom < right_height:
                        overlap_area += (right-left)*(right_height-bottom)
                        val1 = right_height
                    overlap_area += curve(val1, val2, val3, racket_inner)
                bottom += overlap_gap
            left += overlap_gap
    prob = 1-overlap_area/area
    return "%.6f" % prob

def main():
    if testing:
        file_name = 'C-test'
    else:
        file_name = raw_input('Enter file: ')
    try:
        f = open(file_name + '.in', 'rU')
    except:
        print 'File "' + file_name + '.in" does not exist!'
    else:
        inputs = ''
        data = []
        for line in f:
            inputs += line
            if line.strip('\n') != '':
                data.append(line.strip('\n').split())
        f.close()
        output = []
        for i, line in enumerate(data):
            if i > 0:
                output.append('Case #%s: %s' % (i, probability(line)))
        output = '\n'.join(output)
        if testing:
            print output
        else:
            print inputs
            print output
            f = open(file_name + '.out', 'w')
            f.write(output)
            f.close()

main()
