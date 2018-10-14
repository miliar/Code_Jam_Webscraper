#! /usr/bin/python
import re

class BasinMap:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.drainage = [['_d' for i in range(width)] for j in range(height)]

    def calculate_flow_dir(self, map):
        dir = ['_n','_w','_e','_s']
        for i in range(self.height):
            for j in range(self.width):
                low = map[i][j]
                nwes = []
                if i-1 >= 0:
                    nwes.append(map[i-1][j])
                else:
                    nwes.append(10)
                if j-1 >= 0:
                    nwes.append(map[i][j-1])
                else:
                    nwes.append(10)
                try:
                    nwes.append(map[i][j+1])
                except IndexError:
                    nwes.append(10)
                try:
                    nwes.append(map[i+1][j])
                except IndexError:
                    nwes.append(10)

                for k in range(4):
                    if nwes[k] < low:                        
                        self.drainage[i][j] = dir[k]
                        low = nwes[k]

    def follow_dir(self, dir, pos):
        if dir=='n':
            return (pos[0]-1, pos[1])
        if dir=='w':
            return (pos[0], pos[1]-1)
        if dir=='e':
            return (pos[0], pos[1]+1)
        if dir=='s':
            return (pos[0]+1, pos[1])

    def calculate_drainage(self):
        queue = [(i, j) for j in range(self.width) for i in range(self.height)]

        new_drain = ord('a')
        for i in range(self.height):
            for j in range(self.width):
                if self.drainage[i][j] == '_d':
                    queue.remove((i,j))
                    self.drainage[i][j] = '+'+chr(new_drain)
                    new_drain = new_drain + 1
        
        while queue:
            next = queue.pop(0)
            trace = []
            while self.drainage[next[0]][next[1]][0] == '_':
                trace.append(next)
                dir = self.drainage[next[0]][next[1]][1]
                next = self.follow_dir(dir, next)

            for (x,y) in trace:
                self.drainage[x][y] = self.drainage[next[0]][next[1]]

    def correct_labels(self):
        new_label = ord('a')
        old_labels = dict()
        for i in range(self.height):
            for j in range(self.width):
                if self.drainage[i][j][0]=='+':
                    if self.drainage[i][j] in old_labels:
                        self.drainage[i][j] = old_labels[self.drainage[i][j]]
                    else:
                        old_labels[self.drainage[i][j]] = chr(new_label)
                        self.drainage[i][j] = chr(new_label)
                        new_label = new_label + 1

    def print_drainage(self):
        for row in self.drainage:
            print str(row).strip('[').strip(']').replace("'",'').replace(',','')


if __name__ == "__main__":
    n_maps = int(raw_input())
    for i in range(n_maps):
        print 'Case #%d:' % (i+1)

        [h, w] = [int(x) for x in raw_input().split(' ')]
        map = []
        for j in range(h):
            map.append([int(x) for x in raw_input().split(' ')])

        basin = BasinMap(h, w)
        basin.calculate_flow_dir(map)
        basin.calculate_drainage()
        basin.correct_labels()
        basin.print_drainage()

