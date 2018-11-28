#!/usr/bin/env python3

import collections
import functools
import os
import re
import string

from decimal import Decimal


# Based on https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


class CodeJamImpossible:
    def __repr__(self, *args, **kwargs):
        return 'IMPOSSIBLE'


# noinspection PyPep8Naming
class CodeJamBase:
    def __init__(self):
        print(type(self).__name__)
        self.input_file_name, self.output_file_name = self._find_input_and_output_files()
        self.input = None
        self.output = None
        self.pre_compute()
        self._impossible = 'IMPOSSIBLE'

    @staticmethod
    def _find_input_and_output_files():
        """Decide which input file name to use and return it and corresponding output file name.

        :return: input file name and output file name
        """
        files = sorted(list(filter(os.path.isfile, os.listdir('.'))), reverse=True)
        patterns = ['^[A-Z]-large(-(attempt\d?|practice(-\d)?))?\.in$',
                    '^[A-Z]-small(-(attempt\d?|practice(-\d)?))?\.in$',
                    '^sample\.in$']
        for pattern in patterns:
            compiled_pattern = re.compile(pattern)
            for file in files:
                if compiled_pattern.match(file):
                    return file, re.sub('\.in$', '', file) + '.out'
        return 'input.in', 'output.out'

    def __enter__(self):
        print('Reading from {0}, outputting to {1}'.format(self.input_file_name, self.output_file_name))
        self.input = open(self.input_file_name, 'r')
        try:
            self.output = open(self.output_file_name, 'w')
        except:
            self.input.close()
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            try:
                if exc_type is None:
                    data = self.input.read(1024)
                    if data.rstrip('\n'):
                        raise AssertionError('There is still data not read in input file')
            finally:
                self.input.close()
        finally:
            self.output.close()
        return False

    def solve_problem(self, all_needed=False):
        """Solve all cases of a Code Jam problem.

        """

        # Assert we can read from input and output
        if self.input is None or self.output is None:
            raise AssertionError('Input/output file not opened.')

        # Read number of test cases on first line
        first_line = self.input.readline().rstrip('\n')
        if not first_line:
            raise Exception('First line empty in input file')
        n_test_cases = int(first_line)

        # Loop through each case by reading input for it, solving it and outputting the result
        results = []
        for i in range(1, n_test_cases + 1):
            input_vars = self._read_input_for_case(i)
            result = self.solve_case(*input_vars)
            if not all_needed:
                self._write_output_for_case(i, result)
            else:
                results.append(result)

        # If we need all results before we can decide the final result of each case, do the final handling and output
        if all_needed:
            self._change_all_results(results)
            for i in range(1, n_test_cases + 1):
                self._write_output_for_case(i, results[i - 1])

        # Inform the user
        print('Solved!')

    def solve_case(self, *args):
        """Solve a case and return the result ("answer")

        :param args: the case data
        """
        raise NotImplementedError('solve_case not implemented')

    def _change_all_results(self, results):
        pass

    def _read_input_for_case(self, i):
        """Read input for case i and return it

        :param i: case number
        """
        raise NotImplementedError('_read_input_for_case not implemented')

    def _format_case_result(self, result):
        """Format a case result for output in a output file.

        :param result: case answer
        :return: formatted answer for output
        """
        if result is None:
            raise Exception('Case answer should not be None')
        if isinstance(result, CodeJamImpossible) or result is CodeJamImpossible:
            return self._impossible
        if isinstance(result, Decimal):
            if result == Decimal(0):
                return '0.0000000'
            return '{}'.format(result.quantize(Decimal(10) ** -7))
        if isinstance(result, float):
            return "{0:.7f}".format(result)
        if isinstance(result, list):
            return ' '.join((self._format_case_result(x) for x in result))
        return '{0}'.format(result)

    def _write_output_for_case(self, i, result):
        """Output a case result in the output file.

        :param i: case number
        :param result: case answer
        """
        to_output = "Case #{0}: {1}".format(i, self._format_case_result(result))

        self.output.write(to_output + "\n")
        print(to_output)

    def _read_x_lines(self, x=1, split_lines=False, map_func=None):
        """Read x lines from input file and return the lines.

        :param x: number of lines to read
        :param split_lines: split each line with space as separator (default: no)
        :param map_func: function to map on each value (default: no function)
        :return: lines read after optional split and optional map_func
        """
        lines = []
        if split_lines:
            split_lines = ' '
        for j in range(x):
            line = self.input.readline().rstrip('\n')
            if split_lines:
                line = line.split(split_lines)
                if map_func is not None:
                    line = list(map(map_func, line))
            elif map_func is not None:
                line = map_func(line)
            lines.append(line)
        return lines

    def _read_line(self, split_lines=False, map_func=None):
        """Read one line from input file and return the line.

        :param split_lines: split each line with space as separator (default: no)
        :param map_func: function to map on each value (default: no function)
        :return: lines read after optional split and optional map_func
        """
        return self._read_x_lines(1, split_lines, map_func)[0]

    def _read_n_and_x_lines(self, x=None, split_lines=False, map_func=None):
        n = self._read_line(map_func=int)
        if x is None:
            x = n
        return n, self._read_x_lines(x, split_lines, map_func)

    def _read_n_and_first_line(self, split_lines=False, map_func=None):
        n, x = self._read_n_and_x_lines(x=1, split_lines=split_lines, map_func=map_func)
        return n, x[0]

    def _multiple_n_and_repeat_x_lines(self, x=None, split_lines=False, map_func=None):
        all_n = self._read_line(split_lines=True, map_func=int)
        all_lines = []
        for n in all_n:
            current_x = n if x is None else x
            all_lines.append(self._read_x_lines(current_x, split_lines, map_func))
        return all_n, all_lines

    def _repeat_n_and_x_lines(self, x=None, split_lines=False, map_func=None, repeat=2):
        all_N = []
        all_lines = []
        for i in range(repeat):
            N, lines = self._read_n_and_x_lines(x, split_lines, map_func)
            all_N.append(N)
            all_lines.append(lines)
        return all_N, all_lines

    def pre_compute(self):
        pass


class ProblemA(CodeJamBase):
    def __init__(self):
        super().__init__()

    def _read_input_for_case(self, i):
        number_of_parties = self._read_line(map_func=int)
        n_each_party = self._read_line(split_lines=True, map_func=int)
        return number_of_parties, n_each_party

    def solve_case(self, number_of_parties, n_each_party):
        solution = []
        n_each_party = list(n_each_party)
        current_n = sum(n_each_party)
        letters = string.ascii_uppercase
        while current_n:
            taken = [0 for i in range(number_of_parties)]
            if current_n < 3:
                taken = n_each_party
            elif current_n == 3:
                for i, x in enumerate(n_each_party):
                    if x:
                        taken[i] += 1
                        break
                else:
                    raise AssertionError('Did not find one')
            else:
                if_one_no_more_than = (current_n - 1) // 2 + 1
                if_two_no_more_than = (current_n - 2) // 2 + 1
                current_max = max(n_each_party)
                n_parties_current_max = sum(1 for x in n_each_party if n_each_party == current_max)
                for i, x in enumerate(n_each_party):
                    if x == current_max:
                        taken[i] += 1
                        if sum(taken) == 2:
                            break

            solution.append('')
            for i, x in enumerate(taken):
                for j in range(x):
                    solution[-1] += letters[i]
                n_each_party[i] -= x

            current_n = sum(n_each_party)
            if current_n:
                if max(n_each_party)>= (current_n // 2 + 1):
                    print('WARNING WARNING: {}'.format(':'.join([str(z) for z in n_each_party])))
                    raise AssertionError('Solution not correct')

        return ' '.join(solution)


def main():
    with ProblemA() as problem:
        problem.solve_problem(all_needed=False)


if __name__ == "__main__":
    main()
