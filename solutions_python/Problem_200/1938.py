class Case:

    def __init__(self, s, case_num):
        self.s = s
        self.l = list(s)
        self.case_num = case_num
        self.tidy = ''

    def find_tidy(self):
        while not self._is_tidy():
            for i in xrange(len(self.l) - 1):
                if int(self.l[i]) > int(self.l[i + 1]):
                    self.l[i] = str(int(self.l[i]) - 1)
                    for j in xrange(i + 1, len(self.l)):
                        self.l[j] = '9'

        self.tidy = ''.join(self.l)
        self.tidy = int(self.tidy)
        self.tidy = str(self.tidy)

            #print(str(self.l))


    def _is_tidy(self):
        return all(self.l[i] <= self.l[i + 1] for i in xrange(len(self.l) - 1))

    def get_out_line(self):
        return 'Case #' + str(self.case_num) + ': ' + self.tidy + '\n'
