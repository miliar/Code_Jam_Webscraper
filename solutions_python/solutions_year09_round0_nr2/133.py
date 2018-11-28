import sys;

class Map:
    def __init__(self, size, array):
        self.x,self.y = size
        self.sinks = {}
        self.array = array

    def get_adj(self, x,y):
        xs = [i for i in range(x-1,x+2) if i >= 0 if i < self.x]
        ys = [j for j in range(y-1,y+2) if j >= 0 if j < self.y]
        #always returns points in N W E S order
        return [(a,b) for a in xs for b in ys if (a == x) or (b == y)]

    def get_alt(self, x,y):
        return self.array[x][y]

    def _all_points(self):
        return [(x,y) for x in range(self.x) for y in range(self.y)]

    def find_sinks(self):
        for p in self._all_points():
            neighbors = [n for n in self.get_adj(*p) if self.get_alt(*n) <
                    self.get_alt(*p)]
            if len(neighbors) == 0:
                self.sinks[p] = ' '

    def sink_path(self, x, y):
        #return which sink the point (x,y) drains into
        if (x,y) in self.sinks:
            return (x,y)
        adjlist = [(p,self.get_alt(*p)) for p in self.get_adj(x,y)]
        min = adjlist[0]
        for adj in adjlist:
            (p, alt) = adj
            (minp, minalt) = min
            if alt < minalt:
                min = adj
        (spoint, salt) = min
        return self.sink_path(*spoint)

    def label_sinks(self):
        current = ord('a')
        for p in self._all_points():
            sink_point = self.sink_path(*p)
            if self.sinks[sink_point] == ' ':
                self.sinks[sink_point] = chr(current)
                current+=1

    def print_map(self):
        for x in range(self.x):
            row = []
            for y in range(self.y):
                sink = self.sink_path(x,y)
                label = self.sinks[sink]
                row.append(label)
            print ' '.join(row)

cases = [n+1 for n in range(int(sys.stdin.readline().rstrip()))]
for case in cases:
    ht,wd = [int(n) for n in sys.stdin.readline().rstrip().split()]
    map = []
    for i in range(ht):
        row = sys.stdin.readline().rstrip().split()
        map.append([int(n) for n in row])
    m = Map((ht,wd),map)
    m.find_sinks()
    m.label_sinks()
    print "Case #{0}:".format(case)
    m.print_map()
