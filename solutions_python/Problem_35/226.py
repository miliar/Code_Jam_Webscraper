import sys
from numpy import * #http://sourceforge.net/projects/numpy/files/NumPy/1.3.0/numpy-1.3.0.zip/download

max_elevation = 10001

def elevation(t):
    return t[1]

def label(t):
    return t[2]

def neighbors(a, l, y, x):
    return [ ((y,x),a[y,x],l[y,x]) for (y,x) in ((y-1,x), (y,x-1), (y,x+1), (y+1,x)) ]

def min_neighbor(a, l, y, x):
    return min(neighbors(a,l,y,x), key=elevation)

def direction(neighbor, y, x):
    if neighbor[0][0] < y:
        return '1'
    elif neighbor[0][0] > y:
        return '2'
    elif neighbor[0][1] < x:
        return '3'
    else:
        return '4'

def do_map(h,w,rows,n):
        labels = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        a = empty((h+2, w+2), dtype=int32)
        a.fill(max_elevation)
        l = zeros((h+2, w+2), dtype=character)

        for y in range(h):
            for x in range(w):
                a[y+1,x+1] = rows[y][x]

        q = []
        for y in range(1,h+1):
            for x in range(1,w+1):
                m = min_neighbor(a,l,y,x)
                if elevation(m) >= a[y,x]:
                    l[y,x] = labels.pop()
                    q.append((y,x))
                else:
                    l[y,x] = direction(m,y,x)

        while q:
            y,x = q.pop()
            for source in zip(neighbors(a, l, y, x), ('2','4','3','1')):
                if label(source[0]) == source[1]:
                    l[source[0][0][0],source[0][0][1]] = l[y,x]
                    q.append(source[0][0])

        sinks = list(reversed([chr(x) for x in range(ord('a'), ord('z')+1)]))
        labelMap = {}
        print "Case #%d:" % (n+1)
        for y in range(1,h+1):
            for x in range(1,w+1):
                if not labelMap.has_key(l[y,x]):
                    labelMap[l[y,x]] = sinks.pop()
                print labelMap[l[y,x]],
            print ''
    

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for n in range(t):
        h, w = [int(x) for x in sys.stdin.readline().strip().split()]
        rows = []
        for _ in range(h):
            rows.append([int(x) for x in sys.stdin.readline().strip().split()])

        do_map(h,w,rows,n)
