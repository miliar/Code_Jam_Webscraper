import sys


class Cell:

    def __init__(self):
        self.has_x = False
        self.has_p = False
        self.can_x = True
        self.can_p = True

    def __repr__(self):
        if self.has_x:
            if self.has_p: return "o"
            return "x"
        if self.has_p: return "+"
        return "."

#print Cell()


class Platform:

    def __init__(self, size):
        self._cells = [[Cell() for index in range(size)] for index in range(size)]
        self._SIZE = size

    def __repr__(self):
        string =""
        for row in self._cells:
            string += "\n"
            for cell in row:
                string += str(cell)
        return string

    def add_x(self, index, jndex):
        if self._cells[index][jndex].has_x: raise ValueError()
        if not self._cells[index][jndex].can_x: raise ValueError()
        self._cells[index][jndex].has_x = True
        for i in range(self._SIZE):
            self._cells[i][jndex].can_x = False
        for j in range(self._SIZE):
            self._cells[index][j].can_x = False

    def add_p(self, index, jndex):
        if self._cells[index][jndex].has_p: raise ValueError()
        if not self._cells[index][jndex].can_p: raise ValueError()
        self._cells[index][jndex].has_p = True
        i = index
        j = jndex
        while i>=0 and i<self._SIZE and j>=0 and j<self._SIZE:
            self._cells[i][j].can_p = False
            i += 1
            j += 1
        i = index
        j = jndex
        while i>=0 and i<self._SIZE and j>=0 and j<self._SIZE:
            self._cells[i][j].can_p = False
            i -= 1
            j += 1
        i = index
        j = jndex
        while i>=0 and i<self._SIZE and j>=0 and j<self._SIZE:
            self._cells[i][j].can_p = False
            i -= 1
            j -= 1
        i = index
        j = jndex
        while i>=0 and i<self._SIZE and j>=0 and j<self._SIZE:
            self._cells[i][j].can_p = False
            i += 1
            j -= 1

    def add_o(self, index, jndex):
        self.add_x(index, jndex)
        self.add_p(index, jndex)

    def value(self):
        val = 0
        for row in self._cells:
            for cell in row:
                if cell.has_p: val+=1
                if cell.has_x: val+=1
        return val

    def improve(self, start_index=0, start_jndex=0):
        index = start_index
        jndex = start_jndex
        while index < self._SIZE:
            row = self._cells[index]
            while jndex < self._SIZE:
                cell = row[jndex]
                if cell.can_x:
                    if cell.can_p and (index in (0, self._SIZE-1) or jndex in (0, self._SIZE-1)):
                        self.add_o(index, jndex)
                        return "o", index, jndex
                    else:
                        self.add_x(index, jndex)
                        if cell.has_p:
                            return "o", index, jndex
                        else: return "x", index, jndex
                if cell.can_p and (index in (0, self._SIZE-1) or jndex in (0, self._SIZE-1)):
                    self.add_p(index,jndex)
                    if cell.has_x:
                        return "o", index, jndex
                    return "+", index, jndex
                jndex += 1
            jndex = 0
            index += 1
        #print index, jndex
        return "END"




plt = Platform(4)
print plt, plt.value()
plt.add_x(0,0)
plt.add_p(2,3)
plt.add_x(3,3)
print plt, plt.value()
print plt._cells[0][1].can_x
result = plt.improve(0,0)
while not result == "END":
    result = plt.improve(0,0)
    print result
print plt, plt.value()


if __name__ == "__main__" and len(sys.argv) is 2:
    filename = sys.argv[1]
    infile = filename+".in"
    outfile = filename+".out"
    infile = open(infile, "r")
    outfile = open(outfile, "w")
    T = int(infile.readline())
    for case in range(T):
        N, M = infile.readline().split()
        N = int(N)
        M = int(M)
        plt = Platform(N)
        outfile.write("Case #{}: ".format(case+1))
        for model_num in range(M):
            model_type, index, jndex = infile.readline().split()
            index = int(index)-1
            jndex = int(jndex)-1
            if model_type == "o":
                plt.add_o(index, jndex)
            elif model_type == "+":
                plt.add_p(index, jndex)
            elif model_type == "x":
                plt.add_x(index, jndex)
            else: raise ValueError()
        index = 0
        jndex = 0
        result = plt.improve()
        string = ""
        num_improvements = 0
        while not result == "END":
            num_improvements += 1
            print result
            typ, index, jndex = result
            string += "{} {} {}\n".format(typ, index+1, jndex+1)
            result = plt.improve()
        outfile.write("{} {}\n".format(plt.value(), num_improvements))
        outfile.write(string)
        print plt, plt.value()
    infile.close()
    outfile.close()
