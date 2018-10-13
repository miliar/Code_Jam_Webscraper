__author__ = 'bowen'

from os.path import splitext
from sys import setrecursionlimit
from math import *

setrecursionlimit(10000)


class MetaClass(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        #cls.static_variable =


class Solver(object):
    __metaclass__ = MetaClass

    def __init__(self, case_input):
        self.n = int(case_input.readline())
        self.str_list = [case_input.readline().strip() for i in xrange(self.n)]

    def check(self):
        common_meta_str = None
        self.char_count_list = []
        for str_item in self.str_list:
            meta_str = str_item[0]
            char_count = []
            count = 1
            for i in xrange(1, len(str_item)):
                if meta_str[-1] == str_item[i]:
                    count += 1
                    continue
                else:
                    char_count.append(count)
                    count = 1
                    meta_str += str_item[i]
            char_count.append(count)
            self.char_count_list.append(char_count)
            if common_meta_str is None:
                common_meta_str = meta_str
            else:
                if meta_str != common_meta_str:
                    return None
        return common_meta_str

    def solve(self, count):
        cost_sum = 0
        for k in xrange(count):
            total_sum = 0
            for i in xrange(len(self.str_list)):
                total_sum += self.char_count_list[i][k]
            avg = total_sum / float(self.n)
            choice =[floor(avg), ceil(avg)]
            min_cost = None
            for i in choice:
                sum = 0
                for j in xrange(len(self.str_list)):
                    sum += abs(self.char_count_list[j][k] - i)
                if min_cost is None:
                    min_cost = sum
                elif sum < min_cost:
                    min_cost = sum
            #min_cost = None
            #for i in xrange(len(self.str_list)):
            #    sum = 0
            #    for j in xrange(len(self.str_list)):
            #        if i != j:
            #            sum += abs(self.char_count_list[i][k] - self.char_count_list[j][k])
            #    if min_cost is None:
            #        min_cost = sum
            #    elif sum < min_cost:
            #        min_cost = sum
            cost_sum += min_cost
        return cost_sum

    def slove_binary(self):
        x, y = self.str_list
        if x[0] != y[0]:
            return -1
        i = 0
        j = 0
        ch = x[0]
        x_ch = x[0]
        y_ch = y[0]
        count = 0
        while True:
            if i >= len(x) and j >= len(y):
                break
            c_x = 0
            while i < len(x) and x[i] == ch:
                c_x += 1
                i += 1
            c_y = 0
            while j < len(y) and y[j] == ch:
                c_y += 1
                j += 1
            if i < len(x):
                x_ch = x[i]
            if j < len(y):
                y_ch = y[j]
            if x_ch != y_ch:
                return -1
            else:
                ch = x_ch
            count += abs(c_x - c_y)
        return count



    def get_result(self):
        common_meta_str = self.check()
        #print self.str_list[0]
        #print self.str_list[1]
        #print self.slove_binary()
        if common_meta_str is None:
            result = "Fegla Won"
        else:
            count = len(common_meta_str)
            min_cost = self.solve(count)
            result = "%d" % min_cost
        return result


def main(case_input, case_output):
    T = int(case_input.readline())
    for i in xrange(1, T + 1):
        result = Solver(case_input).get_result()
        print 'Case #%d: %s' % (i, result)
        case_output.write('Case #%d: %s\n' % (i, result))

current_path = splitext(__file__)[0]
input_path = current_path + '.in'
output_path = current_path + '.out'

with open(output_path, 'w') as outfile:
    with open(input_path, 'r') as infile:
        main(infile, outfile)