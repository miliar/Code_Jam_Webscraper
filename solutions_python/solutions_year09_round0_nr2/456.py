
import os, sys, re, string

def main():
    N = int(sys.stdin.readline())
    for i in range(N):
        row,col = map(lambda x: int(x), sys.stdin.readline().split(" "))
        wall = [[9999999 for x in range(col + 2)]]
        data = wall + map(lambda x: [99] + map(lambda y: int(y), sys.stdin.readline().split(" ")) + [99], range(row)) + wall
        results = [[0 for x in range(col)] for y in range(row)]
        directions = [[0, -1], [-1, 0], [1,0], [0,1]]
        labels = "abcdefghijklmnopqrstuvwxyz"
        index = [0]
        def get_label():
            v = index[0]
            res = []
            while v >= 26:
                res.append(labels[v % 26])
                v /= 26
            res.append(labels[v])
            res.reverse()
            index[0] += 1
            return "".join(res)
        def get_min_pos(x,y):
            minv = data[y][x]
            res = None
            for d in directions:
                if data[y + d[1]][x + d[0]] < minv:
                    minv = data[y + d[1]][x + d[0]]
                    res = d
            if res:
                return (x + res[0] - 1, y + res[1] - 1)
            return (x-1, y-1)
        def change_label(x, y, label):
            if x >= 0 and x < col and y >= 0 and y < row:
                results[y][x] = label
                lower = get_min_pos(x+1,y+1)
                if lower[0] != x or lower[1] != y:
                    change_label(lower[0], lower[1], label)
                for d in directions:
                    dx = x + d[0]
                    dy = y + d[1]
                    if dx >= 0 and dx < col and dy >= 0 and dy < row and results[dy][dx] == 0:
                        lower = get_min_pos(dx+1, dy+1)
                        if lower[0] == x and lower[1] == y:
                            change_label(dx, dy, label)
        for y in range(row):
            for x in range(col):
                if type(results[y][x]) == int:
                    change_label(x, y, get_label())
        print "Case #%d:" % (i+1)
        for line in results:
            print " ".join(line)
        index[0] = 0
        #for i in range(100):
         #   print i, get_label()

if __name__ == '__main__':
    main()


