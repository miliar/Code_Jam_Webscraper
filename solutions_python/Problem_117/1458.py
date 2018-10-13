class Lawn:

    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols

    def feasible(self, desired):
        """
        (boolean[][]) -> boolean
        
        Checks whether the desired pattern is feasible with given mower.

        The input array is a simplification to the small test data, where
        height of 2 does not need cut but height of 1 does.
        """
        row_conditions = [self.check_line_integrity(desired, lambda arr, x: arr[r][x], self.cols) for r in range(self.rows)]
        col_conditions = [self.check_line_integrity(desired, lambda arr, x: arr[x][c], self.rows) for c in range(self.cols)]

        for r in range(self.rows):
            (is_fine, short) = row_conditions[r]
            if (is_fine): # all cut or all uncut
                continue
            if (reduce(lambda x, y: x and y, map(lambda x: col_conditions[x][0], short), True)): # the col that the cut cell is on is also fine
                continue
            return False

        return True
    
    def check_line_integrity(self, pattern, fn, length):
        """
        (boolean[][], (boolean[][], int) -> boolean, int) -> boolean, int[]

        Checks whether the specified line (by lambda function)
        is cut/uncut all along.
        """
        cut = 0
        short = []
        for x in range(length):
            if (fn(pattern, x)):
                cut += 1
                short.append(x)
        return cut == 0 or cut == length, short


if __name__ == '__main__':
    import sys
    try:
        fname = sys.argv[1]
        try:
            fin = open(fname, 'r')
            case_count = fin.readline()
            for c in range(int(case_count)):
                n, m = map(lambda s: int(s), fin.readline().split(' '))
                lawn = Lawn(n, m) # init first
                desired_lawn = [[False for j in range(m)] for i in range(n)]
                for i in range(n):
                    for j, height in enumerate(fin.readline().split(' ')):
                        desired_lawn[i][j] = (int(height) == 1)
                print "Case #" + str(c + 1) + ":", lawn.feasible(desired_lawn) and 'YES' or 'NO'
        except IOError:
            print "File", fname, "does not exist."
    except IndexError:
        print "Please specify name of the input file."
