#!/usr/bin/env python

import sys

file = open(sys.argv[1])

num_charts = int(file.readline())

def calculate_basins(height, width, chart):
    basins = {}
    labels = {}
    current_label = 0
    for h in xrange(height):
        for w in xrange(width):
            basins[(h,w)] = current_label
            labels[current_label] = {(h,w): True}
            current_label += 1
    for h in xrange(height):
        for w in xrange(width):
            flow = (h,w)
            min_altitude = chart[h][w]
            if h != 0:
                if chart[h-1][w] < min_altitude:
                    min_altitude = chart[h-1][w]
                    flow = (h-1,w)
            if w != 0:
                if chart[h][w-1] < min_altitude:
                    min_altitude = chart[h][w-1]
                    flow = (h,w-1)
            if w != width-1:
                if chart[h][w+1] < min_altitude:
                    min_altitude = chart[h][w+1]
                    flow = (h,w+1)
            if h != height-1:
                if chart[h+1][w] < min_altitude:
                    min_altitude = chart[h+1][w]
                    flow = (h+1,w)
            if flow != (h,w):
                new_label = basins[flow]
                old_label = basins[(h,w)]
                for (h1,w1) in labels[basins[(h,w)]]:
                    basins[(h1,w1)] = new_label
                    labels[new_label][(h1,w1)] = True
    return basins

def show_basins(height, width, chart):
    label_nums = {}
    label_letters = list('abcdefghijklmnopqrstuvwxyz')
    label_letters.reverse()
    basins = calculate_basins(height, width, chart)
    for h in xrange(height):
        for w in xrange(width):
            num_label = basins[(h,w)]
            if num_label not in label_nums:
                label_nums[num_label] = label_letters.pop()
            print label_nums[num_label],
        print

for i in xrange(num_charts):
    height, width = map(int, file.readline().split())
    chart = []
    for line in xrange(height):
        chart.append(map(int, file.readline().split()))
    print 'Case #' + str(i+1) + ':'
    show_basins(height, width, chart)
