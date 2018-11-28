import copy
import itertools
import math
import sys

class Runner(object):
    def __init__(self, file_):
        self._test_cases = None # list<list<int>>
        self._sum_cache = {} # map<tuple<int>, int>
        self._xor_cache = {} # map<tuple<int>, int>

        with open(file_) as f:
            to_ignore = True
            for line in f:
                if self._test_cases == None:
                    self._test_cases = []
                else:
                    if to_ignore:
                        to_ignore = False
                    else:
                        to_ignore = True
                        self._test_cases.append([int(v) for v in line.split(' ')])

#    def _split(self, limit_, all_values_, remaining_value_):
#        result = {} # map<tuple<int>, tuple<int>>
#
#        if len(all_values_) == limit_:
#            result[tuple(sorted(all_values_))] = tuple(sorted(remaining_value_))
#        else:
#            for v in remaining_value_:
#                remaining_value = copy.copy(remaining_value_)
#                all_values = copy.copy(all_values_)
#
#                remaining_value.remove(v)
#                all_values.append(v)
#
#                result.update(self._split(limit_, all_values, remaining_value))
#
#        return result

    def _max_sum(self, v1_, v2_):
        return max(self._sum(v1_), self._sum(v2_))

    def _sum(self, values_):
        return self._sum_cache.setdefault(values_, sum(values_))

    def _xor(self, values_):
        result = self._xor_cache.get(values_, 0)
        if result == 0:
            for v in values_:
                result ^= v
            self._xor_cache[values_] = result

        return result

    def _remaining(self, all_, remove_):
        result = copy.copy(all_)
        for v in remove_:
            result.remove(v)

        return result

    def run(self):
        for i, t in enumerate(self._test_cases):
            result = None
            for j in range(1, int(math.floor(len(t)/2.0)) + 1):
                possibilities = []
                for v in itertools.combinations(t, j):
                    remaining = tuple(self._remaining(t, v))
                    if self._xor(v) == self._xor(remaining):
                        possibilities.append(tuple([v, remaining]))

#                print possibilities

                for p in possibilities:
                    if result == None or self._max_sum(*result) < self._max_sum(*p):
                        result = p

            print 'Case #%d: %s' % (i+1, 'NO' if result == None else self._max_sum(*result))

if __name__ == '__main__':
    Runner(sys.argv[1]).run()
