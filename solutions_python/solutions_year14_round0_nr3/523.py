INITIAL_RATE = 2


class Case(object):
    def __init__(self,R,C,M):
        self.R = R
        self.C = C
        self.M = M
        self.__matrix = []
        for y in xrange(R):
            row = []
            for x in xrange(C):
                row.append('.')
            self.__matrix.append(row)
        #self.__matrix[0][0]='c'
    
    def __copy_matrix(self):
        ret = []
        for y in xrange(len(self.__matrix)):
            row = []
            for x in self.__matrix[y]:
                row.append(x)
            ret.append(row)
        return ret

    def __is_one_click(self):
        mat = self.__do_click(0,0,self.__copy_matrix())
        for x in mat:
            if '.' in x:
                return False
        return True

    def __do_click(self,x,y,mat):
        if y >= len(mat) or y < 0  or x <0  or x >= len(mat[y]):
            return mat
        if mat[y][x] != '.' and mat[y][x] != 'c':
            return mat
        count = 0
        if x > 0:
            if mat[y][x-1] == '*':
                count += 1
            if y > 0:
                if mat[y-1][x-1] == '*':
                    count += 1
            if y < len(mat) -1:
                if mat[y+1][x-1] == '*':
                    count += 1
        if y > 0:
            if mat[y-1][x] == '*':
                count += 1
        if y < len(mat) -1:
            if mat[y+1][x] == '*':
                count += 1
        if x < len(mat[y])-1:
            if mat[y][x+1] == '*':
                count += 1
            if y > 0:
                if mat[y-1][x+1] == '*':
                    count += 1
            if y < len(mat) -1:
                if mat[y+1][x+1] == '*':
                    count += 1
        mat[y][x]=count
        if count == 0:
            mat = self.__do_click(x-1,y-1,mat)
            mat = self.__do_click(x,y-1,mat)
            mat = self.__do_click(x+1,y-1,mat)
            mat = self.__do_click(x-1,y,mat)
            mat = self.__do_click(x+1,y,mat)
            mat = self.__do_click(x-1,y+1,mat)
            mat = self.__do_click(x,y+1,mat)
            mat = self.__do_click(x+1,y+1,mat)
        return mat


    def __solve_recursive(self,x,y,F):
        if F == 0:
            if self.__is_one_click():
                return True
            return False
        while y>=0:
            while x>=0:
                if self.__matrix[y][x] == '*':
                    x -= 1
                    continue
                if x == 1 and F>=2:
                    self.__matrix[y][x]='*'
                    self.__matrix[y][x-1]='*'
                    if self.__is_one_click():
                        new_x=self.C-1
                        new_y = y-1
                        if self.__solve_recursive(new_x,new_y,F-2):
                            return True
                    self.__matrix[y][x]='.'
                    self.__matrix[y][x-1]='.'
                if y == 1 and F>=2:
                    self.__matrix[y][x]='*'
                    self.__matrix[y-1][x]='*'
                    if self.__is_one_click():
                        new_x = x-1%len(self.__matrix[y])
                        new_y = y
                        if new_x == self.C-1:
                            new_y -= 1
                        if self.__solve_recursive(new_x,new_y,F-2):
                            return True
                    self.__matrix[y][x]='.'
                    self.__matrix[y-1][x]='.'
                self.__matrix[y][x]='*'
                if self.__is_one_click():
                    new_x = x-1%len(self.__matrix[y])
                    new_y = y
                    if new_x == self.C-1:
                        new_y -=1
                    if self.__solve_recursive(new_x,new_y,F-1):
                        return True
                self.__matrix[y][x]='.'
                x -= 1
            x =  self.C-1
            y-=1
        return False

    def solve(self):
        if self.M == self.C*self.R-1:
            self.__matrix = []
            for y in xrange(self.R):
                row = []
                for x in xrange(self.C):
                    row.append('*')
                self.__matrix.append(row)
            self.__matrix[0][0]='c'
            self.print_matrix()
            return
        if self.__solve_recursive(self.C-1,self.R-1,self.M):
            self.__matrix[0][0]='c'
            self.print_matrix()
            return
        print 'Impossible'

    def print_matrix(self):
        for row in self.__matrix:
            print ''.join(row)
        
def parse_stdin():
    n = int(raw_input())
    cases = []
    for i in xrange(n):
        c = [int(x) for x in raw_input().split(' ')]
        cases.append(Case(c[0],c[1],c[2]))
    return cases


def main():
    cases = parse_stdin()
    i = 1
    for c in cases:
        print 'Case #{:d}:'.format(i)
        c.solve()
        i += 1


if __name__ == '__main__':
    main()
