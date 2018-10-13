from __future__ import print_function


class Case:
    def __init__(self, r, c, table, case_num):
        self.table = table
        self.r = r
        self.c = c
        self.case_num = case_num
        self.blacklist = []

        self._debug = False


    def calculate(self):
        self._fill()
        result = 'Case #' + str(self.case_num) + ':\n'
        for i in xrange(self.r):
            for j in xrange(self.c):
                result += self.table[i][j]
            result += '\n'
        return result


    def _fill(self):
        for k in xrange(self.r):
            for l in xrange(self.c):
                if self.table[k][l] != '?' and self.table[k][l] not in self.blacklist:
                    self.blacklist.append(self.table[k][l])
                    initial = self.table[k][l]
                    # start = i, j
                    # end = m, n
                    i = k
                    m = k
                    j = l
                    n = l
                    make_sense = True
                    while(make_sense):
                        make_sense = False
                        if self._try_pull_right(i, j, m, n, initial):
                            n += 1
                            make_sense = True
                            self._print_table()
                        if self._try_pull_left(i, j, m, n, initial):
                            j -= 1
                            make_sense = True
                            self._print_table()
                        if self._try_pull_up(i, j, m, n, initial):
                            i -= 1
                            make_sense = True
                            self._print_table()
                        if self._try_pull_down(i, j, m, n, initial):
                            m += 1
                            make_sense = True
                            self._print_table()


    def _try_pull_right(self, i, j, m, n, initial):
        if n + 1 >= self.c:
            return False
        for ind in xrange(i, m + 1):
            if self.table[ind][n + 1] != '?':
                return False
        for ind in xrange(i, m + 1):
            self.table[ind][n + 1] = initial
        return True

    def _try_pull_left(self, i, j, m, n, initial):
        if j - 1 < 0:
            return False
        for ind in xrange(i, m + 1):
            if self.table[ind][j - 1] != '?':
                return False
        for ind in xrange(i, m + 1):
            self.table[ind][j - 1] = initial
        return True

    def _try_pull_up(self, i, j, m, n, initial):
        if i - 1 < 0:
            return False
        for ind in xrange(j, n + 1):
            if self.table[i - 1][ind] != '?':
                return False
        for ind in xrange(j, n + 1):
            self.table[i - 1][ind] = initial
        return True


    def _try_pull_down(self, i, j, m, n, initial):
        if m + 1 >= self.r:
            return False
        for ind in xrange(j, n + 1):
            if self.table[m + 1][ind] != '?':
                return False
        for ind in xrange(j, n + 1):
            self.table[m + 1][ind] = initial
        return True


    def _print_table(self):
        if not self._debug:
            return
        for i in xrange(self.r):
            for j in xrange(self.c):
                print(self.table[i][j], end='')
            print()
        print('_________________')



