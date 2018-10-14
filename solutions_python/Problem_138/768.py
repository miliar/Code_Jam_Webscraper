# tested on python 2.7
# Deceitful War

__author__ = 'purplebear'

from decimal import Decimal


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
        self._fout.close()


def calc_war(n, a_blocks, b_blocks):
    if n == 1:
        # if each has one, the result is
        # pretty much predictable as both
        # have no choice of which blocks to
        # play with.
        if a_blocks[0] < b_blocks[0]:
            result = 0
        else:
            result = 1
    else:
        # this should produce more interesting results...
        a_idx = 0
        b_idx = 0
        b_won = 0
        while a_idx < n and b_idx < n:
            # get first element of naomi blocks
            a_block = a_blocks[a_idx]
            # find b_block that is slightly bigger than a_block
            while b_idx < n:
                if b_blocks[b_idx] > a_block:
                    b_won += 1
                    b_idx += 1
                    break
                b_idx += 1
            a_idx += 1
        result = n - b_won
    return result


def calc_dwar(n, a_blocks, b_blocks):
    if n == 1:
        # if each has one, the result is
        # pretty much predictable as both
        # have no choice of which blocks to
        # play with.
        if a_blocks[0] < b_blocks[0]:
            result = 0
        else:
            result = 1
    else:
        # this should produce more interesting results...
        a_idx = n - 1
        b_idx = n - 1
        a_won = 0
        while a_idx >= 0 and b_idx >= 0:
            # get last element of naomi blocks
            a_block = a_blocks[a_idx]
            # find b_block that is slightly lower than a_block
            while b_idx >= 0:
                if b_blocks[b_idx] < a_block:
                    a_won += 1
                    b_idx -= 1
                    break
                b_idx -= 1
            a_idx -= 1
        result = a_won
    return result



if __name__ == '__main__':

    # input_file = '../inputs/D-sample.in'
    # input_file = '../inputs/D-small-attempt0.in'
    input_file = '../inputs/D-large.in'
    output_file = 'output.txt'

    fr = FileIO(input_file, output_file)

    # read number of cases
    n_cases = int(fr.get_row())

    for n in range(n_cases):
        block_count = fr.get_int()
        naomi_blocks = list(fr.get_float_arrays())
        ken_blocks = list(fr.get_float_arrays())
        naomi_blocks.sort()
        ken_blocks.sort()
        war_result = calc_war(block_count, naomi_blocks, ken_blocks)
        dwar_result = calc_dwar(block_count, naomi_blocks, ken_blocks)
        fr.write('Case #%d: %d %d\n' % (n + 1, dwar_result, war_result,))
    fr.close()
