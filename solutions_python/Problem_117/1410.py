import sys

class lawn:
    def __init__(self, file):
        self.heights = []
        line = file.readline().split(" ")
        self.w = int(line[1])
        self.h = int(line[0])
        
        for y in range(self.h):
            line = file.readline().split()
            row = []
            for x in range(self.w):
                row.append(int(line[x]))
            self.heights.append(row)
    def testMove(self, line):
        state = line[0]
        if state == 100:
            return False
        for x in line[1:]:
            if state != x:
                return False
        return True
    def undoRowMove(self, y):
        i = y-1
        i2 = y+1
        if i < 0:
            i = y+1
        if i >= self.h:
            return
        if i2 >= self.h:
            i2 = i
        heights = self.heights
        result = False
        for x in range(self.w):
            if heights[i][x] > heights[i2][x]:
                if heights[i][x] > heights[y][x]:
                    heights[y][x] = heights[i][x]
                    result = True
            elif heights[i2][x] > heights[y][x]:
                heights[y][x] = heights[i2][x]
                result = True
        return result
    def undoColMove(self, x):
        i = x-1
        i2 = x+1
        if i < 0:
            i = i2
        if i >= self.w:
            return
        if i2 >= self.w:
            i2 = i
        heights = self.heights
        result = False
        for y in range(self.h):
            if heights[y][i] > heights[y][i2]:
                if heights[y][i] > heights[y][x]:
                    heights[y][x] = heights[y][i]
                    result = True
            elif heights[y][i2] > heights[y][x]:
                heights[y][x] = heights[y][i2]
                result = True
        return result
    def printBoard(self):
        for y in range(self.h):
            print(" ".join([str(x) for x in self.heights[y]]))
        print("")
    def getResult(self):
        boardChanged = True
        while boardChanged:
            #self.printBoard()
            boardChanged = False
            for y in range(self.h):
                if self.testMove(self.heights[y]):
                    if self.undoRowMove(y):
                        boardChanged = True
            for x in range(self.w):
                if self.testMove([self.heights[n][x] for n in range(self.h)]):
                    if self.undoColMove(x):
                        boardChanged = True
        #self.printBoard()
        state = self.heights[0][0]
        for x in range(self.w):
            for y in range(self.h):
                if self.heights[y][x] != state:
                    return "NO"
        return "YES"
        
def main():
    #f = open("test", "r")
    f = sys.stdin
    
    num = int(f.readline())
    for i in range(num):
        current = lawn(f)
        print("Case #"+str(i+1)+": ", end='')
        print(current.getResult())

    #f.close()

if __name__ == '__main__':
    main()
