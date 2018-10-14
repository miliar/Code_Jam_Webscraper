#python 3.3

__author__ = 'purplebear'


class FileIO(object):
    """
    Utility to interact with input/output files.
    """

    def __init__(self, input_filename='input.txt', output_filename='output.txt'):
        """
        set the input and output file names.
        """
        self._input = input_filename
        self._output = output_filename
        self._fin = open(self._input, 'r')
        self._fout = open(self._output, 'w')

    def get_row(self):
        """
        get a line row.
        """
        return self._fin.readline().strip('\n').strip(' ')

    def get_int(self):
        return int(self.get_row())

    def get_str_arrays(self):
        """
        get a string array from a line row read from file.
        """
        return self._fin.readline().strip('\n').strip(' ').split(' ')

    def get_int_arrays(self):
        return map(lambda x: int(x), self.get_str_arrays())

    def get_float_arrays(self):
        return map(lambda x: float(x), self.get_str_arrays())

    def write(self, stuffs):
        self._fout.write(stuffs)

    def close(self):
        """
         close used resources.
        """
        self._fin.close()



if __name__ == '__main__':

    input_file = 'A-large.in'
    # input_file = '../inputs/A-large.in'
    output_file = 'output.txt'
    print(__file__)

    fr = FileIO(input_file, output_file)

    # read number of cases
    n_cases = int(fr.get_row())

    for n in range(n_cases):
        row = fr.get_str_arrays()
        smax = int(row[0])
        levels = map(lambda x: int(x), row[1])
        len_levels = len(levels) - 1
        crowd_gathered = levels[0]
        friends_added = 0
        for i in xrange(len_levels):
            level = i + 1
            row_addition = 0
            if crowd_gathered < level:
                row_addition = level - crowd_gathered
            friends_added += row_addition
            crowd_gathered += row_addition + levels[level]

        fr.write('Case #%d: %d\n' % (n + 1, friends_added))
    fr.close()


