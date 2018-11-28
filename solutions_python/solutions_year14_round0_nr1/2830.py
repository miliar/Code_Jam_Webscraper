__author__ = 'prigor'

from cStringIO import StringIO
import sys

class Input(object):
    def __init__(self, raw1, raw2):
        self.index1, self.matrix1 = self.raw_to_matrix(raw1)
        self.index2, self.matrix2 = self.raw_to_matrix(raw2)

    def raw_to_matrix(self, raw):
        raw_io = StringIO("".join(raw))
        index = int(raw_io.readline())
        matrix = {}
        for idx in range(4):
            data = map(lambda x: int(x), raw_io.readline().strip().split())
            matrix[idx+1] = set(data)
        return (index, matrix)

    def calculate(self):
        set_intersect = self.matrix1[self.index1] & self.matrix2[self.index2]
        #print set_intersect
        set_equal = self.matrix1[self.index1] == self.matrix2[self.index2]
	#print set_equal
        if len(set_intersect) == 1 and not set_equal:
            return list(set_intersect)[0]
        elif len(set_intersect) > 1 and set_equal:
            return "Bad magician!"
        elif len(set_intersect) > 1 and not set_equal:
            return "Bad magician!"
        elif len(set_intersect) == 0 and not set_equal:
            return "Volunteer cheated!"
        else:
            return "Uncaught"

ifilename = sys.argv[1]
ifile = file(ifilename, 'r')

N_cases = int(ifile.readline())
data_lines = ifile.readlines()
line_counter = 0
for case in range(N_cases):
    # create input
    raw1 = data_lines[line_counter:line_counter+5]
    line_counter += 5
    raw2 = data_lines[line_counter:line_counter+5]
    line_counter += 5
    i = Input(raw1, raw2)
    print "Case #%s: %s" % (case+1, i.calculate())

