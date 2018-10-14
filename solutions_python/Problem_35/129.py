import sys

N,W,E,S = range(4)
MOVE = ((-1,0),(0,-1),(0,1),(1,0))

class Watersheds:

    def changeMap(self, h, w, map):
        self.h = h
        self.w = w
        self.map = map
        label = "a"
        self.cmap = [[" "]*self.w for i in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                if self.cmap[y][x] == " ":
                    yy, xx = y, x
                    cells = set()
                    while True:
                        cells.add((yy,xx))
                        ret = self.move(yy, xx)
                        if ret == None or ret in cells:
                            self.setLabel(cells,label)
                            label = chr(ord(label)+1)
                            break
                        yy,xx = ret
                        if self.cmap[yy][xx] != " ":
                            self.setLabel(cells,self.cmap[yy][xx])
                            break
        return self.cmap
    
    def move(self, y, x):
        next = None
        min = self.map[y][x]
        for i in range(4):
            yy = y + MOVE[i][0]
            if yy < 0 or yy >= self.h:
                continue
            xx = x + MOVE[i][1]
            if xx < 0 or xx >= self.w:
                continue
            if min > self.map[yy][xx]:
                next = (yy, xx)
                min = self.map[yy][xx]
        return next
    
    def setLabel(self, cells, label):
        for cell in cells:
            self.cmap[cell[0]][cell[1]] = label

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        nums = sys.stdin.readline().split()
        map = []
        for j in range(int(nums[0])):
            row = sys.stdin.readline().split()
            r = []
            for cell in row:
                r.append(int(cell))
            map.append(r)
        ret = Watersheds().changeMap(int(nums[0]), int(nums[1]), map)
        print("Case #%d:" % (i+1))
        for row in ret:
            print(" ".join(row)) 


if __name__ == "__main__":
    main()