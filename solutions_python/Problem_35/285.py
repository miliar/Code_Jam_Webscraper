from string import lowercase

class Matrix(object):
    
    def __init__(self, width, height):
        self.matrix = []
        self.width = width
        self.height = height
        for i in xrange(height):
            self.matrix.append([None] * width)
            
    def set_row(self, row_index, values):
        if len(values) == self.width and row_index < self.height:
            for value in values:
                self.matrix[row_index] = values
                
    def rows(self):
        return self.matrix
            
    def get_value(self, x, y):
        return self.matrix[y][x]
    
    def set_value(self, x, y, value):
        self.matrix[y][x] = value
        
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.rows()])

class Basins(Matrix):
    
    def __init__(self, width, height):
        Matrix.__init__(self, width, height)
        self.next_label_index = 0
        
    def get_next_label(self):
        label = lowercase[self.next_label_index]
        self.next_label_index += 1
        return label
    
    def set_next_value(self, x, y):
        value = self.get_next_label()
        self.set_value(x, y, value)
        return value

class Watersheds(object):
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.basins = Basins(self.matrix.width, self.matrix.height)

    def neighbors(self, x, y):
        if y > 0:
            yield x, y - 1
        if x > 0:
            yield x - 1, y
        if x < self.matrix.width - 1:
            yield x + 1, y
        if y < self.matrix.height - 1:
            yield x, y + 1
            
    def find_best_neighbor(self, x, y):
        best = None
        cell = self.matrix.get_value(x, y)
        for nx, ny in self.neighbors(x, y):
            neighbor = self.matrix.get_value(nx, ny)
            if neighbor < cell and (best is None or neighbor < best[2]):
                best = (nx, ny, neighbor)
        return best
    
    def flow(self, x, y):
        neighbor = self.find_best_neighbor(x, y)
        if neighbor is None:
            label = self.basins.get_value(x, y)
            if label is None:
                return self.basins.set_next_value(x, y)
            return label
        nx, ny, value = neighbor
        label = self.flow(nx, ny)
        self.basins.set_value(x, y, label)
        return label
    
    def calculate_basins(self):
        for y, row in enumerate(self.matrix.rows()):
            for x, altitude in enumerate(row):
                if self.basins.get_value(x, y) is None:
                    self.flow(x, y)
        return self.basins

def read(filename):
    input = open(filename, 'r')
    
    tests_num = int(input.readline().strip())
    tests = []
    
    for t in xrange(tests_num):
        height, width = map(int, input.readline().strip().split(" "))
        matrix = Matrix(width, height)
        for i in xrange(height):
            matrix.set_row(i, [int(entry) for entry in input.readline().strip().split(" ")])
        tests.append(matrix)
    
    input.close()
    
    return tests

if __name__ == "__main__":
    tests = read('B-large.in')
    
    for index, test in enumerate(tests):
        print "Case #%d:" % (index + 1)
        ws = Watersheds(test)
        print ws.calculate_basins()