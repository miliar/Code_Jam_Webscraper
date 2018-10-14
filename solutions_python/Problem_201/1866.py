# from Stall import *


class Case:
    def __init__(self, n, k, case_num):
        self.n = int(n)
        self.k = int(k)
        self.case_num = case_num
        # self.stalls = []
        # for i in xrange(n + 2):
        #     self.stalls.append(Stall())
        # self.stalls[-1].occupied = True
        # self.stalls[0].occupied = True
        self.windows = [self.n]
        self.min = 0
        self.max = 0


    def calculate(self):
        for i in xrange(self.k - 1):
            self._add_user()
        self._add_last_user()
        result = 'Case #' + str(self.case_num) + ': ' + str(self.max) + ' ' + str(self.min) + '\n'
        print(result)
        return result


    def _add_user(self):
        max_win = self._find_max_win()
        w = max_win / 2

        if max_win % 2 == 0:
            self.windows.append(w)
            self.windows.append(w - 1)
        else:
            self.windows.append(w)
            self.windows.append(w)


    def _add_last_user(self):
        max_win = self._find_max_win()
        w = max_win / 2
        self.max = w
        if max_win % 2 == 0:
            self.min = w - 1
        else:
            self.min = w


    def _find_max_win(self):
        max_win_ind = 0
        max_win_val = self.windows[0]

        for i in xrange(len(self.windows)):
            if self.windows[i] > max_win_val:
                max_win_val = self.windows[i]
                max_win_ind = i

        return self.windows.pop(max_win_ind)