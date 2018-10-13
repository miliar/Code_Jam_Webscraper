class Lawn:
    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width
        self.area = []

    def addRow(self, areaList):
        self.area.append(areaList)

    def isPossible(self):
        for x in range(self.height):
            for y in range(self.width):
                if not self.isPossibleArea(x, y):
                    return "NO"
        return "YES"
    
    def isPossibleArea(self, height, width):
        limit = self.area[height][width]

        heightValid = True
        widthValid = True
        
        for i in range(self.height):
            if self.area[i][width] > limit:
                heightValid = False
                break;

        if not heightValid:
            for i in range(self.width):
                if self.area[height][i] > limit:
                    widthValid = False
                    break;

        return heightValid or widthValid
        
class Content:
    def __init__(self):
        self.content = self.getFile()
        self.counter = 0
        self.count = 0
        self.cases = []

    def process(self):
        self.count = int(self.getLine())
        line = self.getLine()
        while line != "":
            dimension = line.split(" ")
            height = int(dimension[0])
            width = int(dimension[1])
            area = Lawn(height, width)
            for i in range(height):
                row = self.getLine().split(" ")
                area.addRow(row)
            self.cases.append(area)
            line = self.getLine()

    def getLine(self):
        self.counter += 1
        return self.content[self.counter - 1]

    def getFile(self):
        with open("B-small-attempt1.in", "r") as f:
            return f.read().split("\n")

def run():
    data = Content()
    data.process()

    counter = 1
    with open("output.txt", "w") as f:
        for i in data.cases:
            f.write("Case #" + str(counter) + ": " + i.isPossible() + "\n")
            counter += 1

run()
