#!/usr/bin/python2.7


from decimal import Decimal
from collections import Counter


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

    def get_decimal_arrays(self):
        return map(lambda x: Decimal(x), self.get_str_arrays())

    def write(self, stuffs):
        self._fout.write(stuffs)

    def close(self):
        """
         close used resources.
        """
        self._fin.close()
        self._fout.close()


def find_result(a, b, k):
    sum = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                sum += 1
    return sum


if __name__ == '__main__':
    # fio = FileIO('../inputs/B-sample.in')
    fio = FileIO('../inputs/B-small-attempt0.in')
    n_cases = fio.get_int()
    for n in range(n_cases):
        values = fio.get_int_arrays()
        a = values[0]
        b = values[1]
        k = values[2]
        result = find_result(a, b, k)
        # print('Case #%d: %d' % (n + 1, result,))
        fio.write('Case #%d: %d\n' % (n + 1, result,))
    fio.close()

