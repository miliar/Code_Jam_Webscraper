'''
Created on 2012/04/14

@author: hanaue51
'''
import os, math
os.chdir("../../../data/2012/qualification/")
filename = "D-small-attempt2"
postfix_in = ".in"
postfix_out = ".out"
format = "Case #%d: %d\n"

infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

n_cases = int(lines[0].strip())
results = []
i = 1
case = 1
while i < len(lines):
    elems = lines[i].strip().split()
    height = int(elems[0])
    width = int(elems[1])
    distance = int(elems[2])
    map = []
    x = 0
    y = 0
    for j in xrange(height):
        i += 1
        map.append(lines[i].strip())
        if 'X' in lines[i]:
            y = 0.5 + j - 1
            x = 0.5 + lines[i].index('X') - 1
    left = d_left = x
    right = d_right = width - 2 - x
    top = d_top = y
    bottom = d_bottom = height - 2 - y
    answer = 0
    if 2 * top <= distance: answer += 1
    if 2 * bottom <= distance: answer += 1
    if 2 * left <= distance: answer += 1
    if 2 * right <= distance: answer += 1
    py = 0
    angles = []
    while abs(py - y) <= distance:
        d_top, d_bottom = d_bottom, d_top
        py -= d_bottom
        px = 0
        while abs(px - x) <= distance:
            d_left, d_right = d_right, d_left
            px -= d_right
            if math.sqrt((px - x) ** 2 + (py - y) ** 2) <= distance:
                angle = math.atan2(py - y, px - x)
                if angle not in angles:
                    angles.append(angle)
                    answer += 1
            else:
                break
            px -= d_left
        px = width - 2
        d_left, d_right = left, right
        while abs(px - x) <= distance:
            d_left, d_right = d_right, d_left
            px += d_left
            if math.sqrt((px - x) ** 2 + (py - y) ** 2) <= distance:
                angle = math.atan2(py - y, px - x)
                if angle not in angles:
                    angles.append(angle)
                    answer += 1
            else:
                break
            px += d_right
        d_left, d_right = left, right
        py -= d_top
    py = height - 2
    d_top, d_bottom = top, bottom
    while abs(py - y) <= distance:
        d_top, d_bottom = d_bottom, d_top
        py += d_top
        px = 0
        while abs(px - x) <= distance:
            d_left, d_right = d_right, d_left
            px -= d_right
            if math.sqrt((px - x) ** 2 + (py - y) ** 2) <= distance:
                angle = math.atan2(py - y, px - x)
                if angle not in angles:
                    angles.append(angle)
                    answer += 1
            else:
                break
            px -= d_left
        px = width - 2
        d_left, d_right = left, right
        while abs(px - x) <= distance:
            d_left, d_right = d_right, d_left
            px += d_left
            if math.sqrt((px - x) ** 2 + (py - y) ** 2) <= distance:
                angle = math.atan2(py - y, px - x)
                if angle not in angles:
                    angles.append(angle)
                    answer += 1
            else:
                break
            px += d_right
        py += d_bottom
        d_left, d_right = left, right
    results.append(format % (case, answer))
    i += 1
    case += 1

#print results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
