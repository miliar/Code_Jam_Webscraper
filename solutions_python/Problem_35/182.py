#!python

alphabet = "abcdefghijklmnopqrstuvwxyz"

def sink_compare(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[1] < b[1]:
        return -1
    return 1


import sys

if len(sys.argv) != 2:
    print "Must take only a filename as an argument."
    exit(-1)

filename = sys.argv[1]
fh = open(filename, 'r')
fn = fh.read().split('\n')

num_maps = int(fn[0])
fn = fn[1:]

for m in xrange(0, num_maps):
    format = fn[0].split()
    rows = int(format[0])
    cols = int(format[1])

    curr_map = []

    for r in xrange(0, rows):
        curr_map.append([])
        curr_row = fn[1+r].split()
        for c in xrange(0, cols):
            curr_elt = int(curr_row[c])
            curr_map[r].append(curr_elt)

    sinks = []
    for i in xrange(0, rows):
        for j in xrange(0, cols):
            c = curr_map[i][j]
            n = curr_map[max(i-1, 0)][j]
            w = curr_map[i][max(j-1, 0)]
            e = curr_map[i][min(j+1, cols-1)]
            s = curr_map[min(i+1, rows-1)][j]
            if n >= c and w >= c and e >= c and s >= c:
                sinks.append((i, j))

    sink_labels = {}

    labels = []
    for r in xrange(0, rows):
        labels.append([])
        for c in xrange(0, cols):
            p = (r, c)
            while p not in sinks:
                lowest_index = p
                lowest_val = curr_map[p[0]][p[1]]
                n = curr_map[max(p[0]-1, 0)][p[1]]
                if n < lowest_val:
                    lowest_val = n
                    lowest_index = (p[0]-1, p[1])
                w = curr_map[p[0]][max(p[1]-1, 0)]
                if w < lowest_val:
                    lowest_val = w
                    lowest_index = (p[0], p[1]-1)
                e = curr_map[p[0]][min(p[1]+1, cols-1)]
                if e < lowest_val:
                    lowest_val = e
                    lowest_index = (p[0], p[1]+1)
                s = curr_map[min(p[0]+1, rows-1)][p[1]]
                if s < lowest_val:
                    lowest_val = s
                    lowest_index = (p[0]+1, p[1])
                p = lowest_index
            if len(sink_labels.keys()) != 26:
                sink_labels.setdefault(p, alphabet[len(sink_labels.keys())])

            labels[r].append(sink_labels[p])

    print "Case #%d:" % (m+1)
    for r in xrange(0, rows):
        if r:
            print ""
        for c in xrange(0, cols):
            if c:
                print " ",
            print labels[r][c],
    print ""

    fn = fn[1+rows:]


fh.close()
