import sys

lines = [line for line in sys.stdin]

n_cases = int(lines[0])

LINES_PER_CASE = 1+4+1+4

class Case:
    def __init__(self, lines, case_num):
        start = case_num*LINES_PER_CASE+1
        i = int(lines[start])
        row_one = set(int(x) for x in lines[start+i].split(' '))
        j = int(lines[start+5])
        row_two = set(int(x) for x in lines[start+5+j].split(' '))
        combined = row_one & row_two
        if len(combined) == 0:
            self.result = "Volunteer cheated!"
        elif len(combined) == 1:
            self.result = combined.pop()
        elif len(combined) > 1:
            self.result = "Bad magician!"

    def get_result(self):
        return self.result

for i_case in xrange(n_cases):
    case = Case(lines, i_case)
    print("Case #%d: %s" % (i_case+1, case.get_result()))
