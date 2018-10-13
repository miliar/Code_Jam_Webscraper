__author__ = 'anze'


class Case:
    first_choice = None
    scond_choice = None
    first_matrix = []
    scond_matrix = []

    def __init__(self, f):
        self.first_matrix = []
        self.scond_matrix = []
        self._read_first_case(f)
        self._read_second_case(f)

    def _read_first_case(self, input_file):
        self.first_choice = int(input_file.readline().replace('\n', ''))-1
        for x in range(4):
            self.first_matrix.append(input_file.readline().replace('\n', '').split(' '))

    def _read_second_case(self, input_file):
        self.scond_choice = int(input_file.readline().replace('\n', ''))-1
        for x in range(4):
            self.scond_matrix.append(input_file.readline().replace('\n', '').split(' '))

    def get_the_card(self):
        first = set(self.first_matrix[self.first_choice])
        second = set(self.scond_matrix[self.scond_choice])
        intersection = first.intersection(second)

        if len(intersection) == 0:
            return "Volunteer cheated!"
        elif len(intersection) == 1:
            return list(intersection)[0]
        else:
            return "Bad magician!"

f = open('A-small-attempt0.in')
cases = int(f.readline().replace('\n', ''))

for case in range(cases):
    c = Case(f)
    print "Case #%d: %s" % (case + 1, c.get_the_card())
