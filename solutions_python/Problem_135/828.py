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

    def write(self, stuffs):
        self._fout.write(stuffs)

    def close(self):
        """
         close used resources.
        """
        self._fin.close()
        self._fout.close()


BOARD_SIZE = 4

if __name__ == '__main__':

    input_file = 'A-small-attempt0.in'
    output_file = 'output.txt'

    fr = FileIO(input_file, output_file)

    # read number of cases
    n_cases = int(fr.get_row())

    for n in range(n_cases):

        first_answer = fr.get_int()
        for i in range(BOARD_SIZE):
            number_row = fr.get_int_arrays()
            if i == first_answer - 1:
                first_set = set(number_row)
            # print(number_row)
        
        second_answer = fr.get_int()
        for i in range(BOARD_SIZE):
            number_row = fr.get_int_arrays()
            if i == second_answer - 1:
                second_set = set(number_row)

        x = [first_set, second_set]
        y = set.intersection(*x)
        len_y = len(y)
        if len_y == 1:
            fr.write('Case #%d: %d\n' % (n + 1, y.pop(),))
        elif len_y > 1:
            fr.write('Case #%d: Bad magician!\n' % (n + 1))
        else:
            fr.write('Case #%d: Volunteer cheated!\n' % (n + 1))

    fr.close()
