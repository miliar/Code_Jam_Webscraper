NORTH = -1, 0
WEST = 0, -1
EAST = 0, 1
SOUTH = 1, 0

def get_parents(H, W, altitudes):
    parents = [[None] * W for _ in xrange(H)]
    for y in xrange(H):
        for x in xrange(W):
            z = altitudes[y][x]
            neighbors = []
            for dy, dx in NORTH, WEST, EAST, SOUTH:
                y2, x2 = y + dy, x + dx
                if 0 <= y2 < H and 0 <= x2 < W:
                    z2 = altitudes[y2][x2]
                else:
                    z2 = 10000
                neighbors.append([z2, y2, x2])
            z2, y2, x2 = min(neighbors)
            if z2 < z:
                parents[y][x] = y2, x2
    return parents

def set_labels(y, x, parents, labels, next_label):
    label = labels[y][x]
    if label is None:
        if parents[y][x] is None:
            label = next_label()
        else:
            y0, x0 = parents[y][x]
            label = set_labels(y0, x0, parents, labels, next_label)
        labels[y][x] = label
    return label

def get_labels(H, W, parents):    
    labels = [[None] * W for _ in xrange(H)]
    next_label = iter('abcdefghijklmnopqrstuvwxyz').next
    for y in xrange(H):
        for x in xrange(W):
            set_labels(y, x, parents, labels, next_label)
    return labels

def solve(H, W, altitudes):
    parents = get_parents(H, W, altitudes)
    return get_labels(H, W, parents)

def main():
    T = int(raw_input())
    for case in xrange(T):
        H, W = map(int, raw_input().split())
        altitudes = [map(int, raw_input().split()) for _ in xrange(H)]
        print 'Case #%d:' % (case + 1)
        for row in solve(H, W, altitudes):
            print ' '.join(row)

if __name__ == '__main__':
    main()
