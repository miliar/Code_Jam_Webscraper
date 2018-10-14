class Lawn:
    def __init__(self, matrix):
        self.pattern = matrix
        self.rows = len(self.pattern)
        self.columns = len(self.pattern[0])
        self.lowest = 100
        for i in self.pattern:
            for j in i:
                if self.lowest > j:
                    self.lowest = j

    def analizeRow(self, row):
        for i in self.pattern[row]:
            if i>self.lowest:
                return False
        return True
    
    def analizeColumn(self, column):
        for i in self.pattern:
            if i[column] > self.lowest:
                return False
        return True
    
    def nextLowest(self):
        if self.lowest == 100:
            return True
        newLowest = 100
        for i in self.pattern:
            for j in i:
                if newLowest > j and self.lowest < j:
                    newLowest = j
        self.lowest = newLowest
        return False
    
    def analizeCell(self, row, column):
        valid = self.analizeRow(row)
        if not valid:
            valid = self.analizeColumn(column)
        return valid
    
    def isPossible(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.pattern[i][j] == self.lowest:
                    if not self.analizeCell(i, j):
                        return "NO"
        if self.nextLowest():
            return "YES"
        return self.isPossible()
    
if __name__ == '__main__':
    fi = open("B-large.in")
    text = fi.read().split()
    cases = int(text[0])
    del text[0]
    for case in range(cases):
        rows = int(text[0])
        del text[0]
        columns = int(text[0])
        del text[0]
        lawn = [[100 for i in range(columns)]for j in range(rows)]
        for i in range(rows):
            for j in range(columns):
                lawn[i][j] = int(text[0])
                del text[0]
        yard = Lawn(lawn)
        print "Case #" + str(case+1) + ": " + yard.isPossible()
    pass