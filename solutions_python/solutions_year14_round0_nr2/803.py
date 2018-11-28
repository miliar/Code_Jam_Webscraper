# tested on python 2.7

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


if __name__ == '__main__':

    # input_file = 'B-small-attempt0.in'
    input_file = 'B-large.in'
    # input_file = 'input.sample.txt'
    output_file = 'output.txt'

    fr = FileIO(input_file, output_file)

    # read number of cases
    n_cases = int(fr.get_row())

    for n in range(n_cases):
        values = fr.get_float_arrays()
        farm_price = values[0]  # c
        farm_incr = values[1]   # f
        time_to_win = values[2] # x
        rate = 2.0
        # print('%g %g %g' % (farm_price, farm_incr, time_to_win,))

        # how much we get if not buying farm
        buy_more = True
        time_ofs = 0
        while buy_more:
            t_notbuying = time_ofs + time_to_win / rate
            buying_time = farm_price / rate
            rate_afterbuy = rate + farm_incr
            t_buying = time_ofs + buying_time + (time_to_win / rate_afterbuy)
            if t_notbuying < t_buying:
                buy_more = False

            rate = rate_afterbuy
            time_ofs = time_ofs + buying_time
        fr.write('Case #%d: %.08g\n' % (n + 1, t_notbuying,))
    fr.close()
