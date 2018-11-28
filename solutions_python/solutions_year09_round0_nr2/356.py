#!/usr/bin/python2.5

# return in NWES order
def get_neighbors(i, j, H, W):
    neighbors = []
#   N
    if (i>0): neighbors.append((i-1,j))

#   W
    if (j>0): neighbors.append((i,j-1))

#   E
    if (j<W-1): neighbors.append((i,j+1))

#   S
    if (i<H-1): neighbors.append((i+1,j))

    return neighbors

def is_sink(i, j, H, W, altitude):
    for neighbor in get_neighbors(i, j, H, W):
        if (altitude[neighbor] < altitude[i,j]):
            return False
    return True

def get_min_neighbor(i, j, H, W, altitude):
    first_time = True
    neighbors = get_neighbors(i, j, H, W)
    for neighbor in neighbors:
        if (first_time or altitude[neighbor] < min_altitude):
            min_neighbor = neighbor
            min_altitude = altitude[neighbor]
            first_time = False
    return min_neighbor

def assign_to_sink(i, j, H, W, altitude, assignedSink):
    if ((i,j) in assignedSink): return
    min_neighbor = get_min_neighbor(i, j, H, W, altitude)
    if not min_neighbor in assignedSink:
        assign_to_sink(min_neighbor[0], min_neighbor[1], H, W, altitude, assignedSink)
    assignedSink[i,j] = assignedSink[min_neighbor]

T = input()
for case in range(T):
    print 'Case #%d: ' % (case+1)

    altitude = {}
    assignedSink = {}
    latest_sink_id = 1
    latest_sink_label = 'a'
    label = {}
    sink_id_to_label = {}

    (H, W) = map(int, raw_input().split())
    for i in range(H):
        j = 0
        for elem in raw_input().split():
            altitude[i,j] = elem
            j += 1

    for i in range(H):
        for j in range(W):
            if (is_sink(i, j, H, W, altitude)):
                assignedSink[i,j] = latest_sink_id
                latest_sink_id += 1 

    for i in range(H):
        for j in range(W):
            assign_to_sink(i, j, H, W, altitude, assignedSink)

    for i in range(H):
        for j in range(W):
            sink_id = assignedSink[i,j]
            if not (sink_id in sink_id_to_label):
                sink_id_to_label[sink_id] = latest_sink_label
                latest_sink_label = chr(ord(latest_sink_label)+1)
            label[i,j] = sink_id_to_label[sink_id]

    for i in range(H):
        for j in range(W):
            print label[i,j],
        print
