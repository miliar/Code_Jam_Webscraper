#!/usr/bin/python

def run(R, k, N, g):
    earned = 0
    round = 0
    history = []
    current = 0
    group_num = len(g)

    for i in xrange(R):
        sum = 0
        start_index = current
        while True:
            if sum != 0 and start_index == current:
                break
            elif sum + g[current] <= k:
                sum = sum + g[current]
                current = current + 1
                if current == group_num:
                    current = 0
            else:
                break
        earned = earned + sum

    return earned 

input_file = file('C-small-attempt0.in')
output_template = "Case #%d: %d"
T = int(input_file.readline())

for i in xrange(T):
    index = i + 1
    line = map(int, input_file.readline().split())
    g = map(int, input_file.readline().split())

    earned = run(line[0], line[1], line[2], g)

    print output_template % (index, earned)
