FILE_IN = "B-large.in"
FILE_OUT = "B-large.out"
NEWLINE = '\n'
DEBUG = False

from datetime import datetime

class Lawn(object):
    def __init__(self, lines ,n1, n2):
        self.rows = []
        self.max_elem_in_row = []
        self.max_elem_in_col = []
        self.columns = []
        for i in range(n2):
            self.columns.append([])
        for i in range(n1):
            l = lines[i].strip()
            l = l.split(" ")
            self.rows.append([int(j) for j in l])
            self.max_elem_in_row.append(max(self.rows[i]))
            for j in range(n2):
                self.columns[j].append(self.rows[i][j])
        for column in self.columns:
            self.max_elem_in_col.append(max(column))
    
    def solve(self):
        rows_num = len(self.rows)
        cols_num = len(self.columns)
        for i in range(rows_num):
            for j in range(cols_num):
                x = self.rows[i][j]
                if x < self.max_elem_in_row[i] and x < self.max_elem_in_col[j]:
                    return "NO"                
        return "YES"
                    
if __name__ == '__main__':
    print "started at: " + str(datetime.now())
    f = open(FILE_IN, "r")
    f_out = open(FILE_OUT, "w")
    lines = f.readlines()
    num_of_cases = int(lines[0])
    j = 1
    lines_out = []
    
    for i in range(num_of_cases):
        if DEBUG:
            print i
        sizes = lines[j].strip()
        sizes = sizes.split(" ")
        sizes = [int(t) for t in sizes]
        r = sizes[0]
        c = sizes[1]
        data  = lines[j+1:j+1+r]
        j += 1 + r
        l = Lawn(data, sizes[0], sizes[1])      
        ans = l.solve()
        result = "Case #%d: " % (i+1) + ans + NEWLINE
        lines_out.append(result)

    f_out.writelines(lines_out)
    f.close()
    f_out.close()
    print 'done.'
    print "ended at: " + str(datetime.now())
