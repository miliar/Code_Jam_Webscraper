class DataReader:
    def __init__(self, input_filename):
        self.data = [x.strip() for x in open(input_filename)]
        self.curr_line = 0
        
    def read_line(self):
        data = self.data[self.curr_line]
        self.curr_line += 1
        return data

    def read_int(self):
        return int(self.read_line())
    
    def read_ints(self):
        line = self.read_line()
        return [int(x) for x in line.split()]

class DataWriter:
    def __init__(self, output_filename):
        self.lines = []
        self.output_filename = output_filename
        self.num_case = 1

    def write_line(self, line):
        self.lines.append("%s\n" % line)

    def write_line(self, data):
        self.lines.append("Case #%i: %s\n" % (self.num_case, data))
        self.num_case += 1

    def write_ints(self, ints):
        self.write_line(" ".join([str(x) for x in ints]))

    def flush(self):
        open(self.output_filename, "w").writelines(self.lines)

MOWED = 101

def min_elem(data):
    return min([min(x) for x in data])

def has_elem(data):
    return min_elem(data) != MOWED

def get_pivot_row(data, pivot):
    empty_set = set([MOWED])
    accepted = set([pivot, MOWED])
    
    for idx, row in enumerate(data):
        row_set = set(row)
        if row_set.issubset(accepted) and not row_set.issubset(empty_set):
            return idx
    return -1

def get_pivot_col(data, pivot):
    empty_set = set([MOWED])
    accepted = set([pivot, MOWED])
    num_rows = len(data)
    num_cols = len(data[0])

    for col_id in xrange(num_cols):
        col = [data[x][col_id] for x in xrange(num_rows)]
        col_set = set(col)
        if col_set.issubset(accepted) and not col_set.issubset(empty_set):
            return col_id
    return -1

def has_pivot_line(data, pivot):
    return get_pivot_row(data, pivot) != -1 or get_pivot_col(data, pivot) != -1

def mow_row(data, row_num):
    num_cols = len(data[0])
    for i in xrange(num_cols):
        data[row_num][i] = MOWED

def mow_col(data, col_num):
    num_rows = len(data)
    for i in xrange(num_rows):
        data[i][col_num] = MOWED
    

def mow_pivot_line(data, pivot):
    pivot_row  = get_pivot_row(data, pivot)
    if pivot_row != -1:
        mow_row(data, pivot_row)
        return

    pivot_col = get_pivot_col(data, pivot)
    mow_col(data, pivot_col)

def can_mow(data):
    while has_elem(data):
        pivot = min_elem(data)
        if has_pivot_line(data, pivot):
            mow_pivot_line(data, pivot)
        else:
            return False
        
    return True

def solve(input_filename, output_filename):
    reader = DataReader(input_filename)
    writer = DataWriter(output_filename)

    num_cases = reader.read_int()
    for i in xrange(num_cases):
        height,width = reader.read_ints()
        data = []
        for x in xrange(height):
            data.append(reader.read_ints())

        if can_mow(data):
            print "Case #%s: YES" % (i+1)
            writer.write_line("YES")
        else:
            print "Case #%s: NO" % (i+1)
            writer.write_line("NO")

    writer.flush()

#if __name__ == '__main__':
#    solve("example.in", "example.out")
