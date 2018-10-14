# /usr/bin/env python
# -*- coding: utf8 -*-

IMP = "IMPOSSIBLE"
HAPPY = "+"
BLANK = "-"


def convert_row_to_int(row):
    return [1 if p == HAPPY else -1 for p in row]


def convert_int_to_row(int_row):
    return "".join([HAPPY if p == 1 else BLANK for p in int_row])


class PancakeRow:

    __slots__ = ("row",
                 "step",
                 "size_row",
                 "eval_state",
                 "previous_pos")
    fsize = None

    def __init__(self,
                 s,
                 k,
                 step=0,
                 previous_pos=None):
        self.row = s
        self.step = step
        self.size_row = len(s)
        self.eval_state = self.row.count(1)
        self.previous_pos = previous_pos

    def all_happy(self):
        return self.eval_state == self.size_row

    def flip(self, pos):
        if pos == self.previous_pos:
            # print("REJECTED ppos", convert_int_to_row(self.row), pos)
            return None
        if self.size_row - pos < self.fsize:
            # print("REJECTED hight pos", convert_int_to_row(self.row), pos, (self.size_row - pos, self.fsize))
            return None
        else:
            new_row = [-1 * p if pos <= i < pos +
                       self.fsize else p for i, p in enumerate(self.row)]
            return PancakeRow(new_row,
                              self.fsize,
                              step=self.step + 1,
                              previous_pos=pos)


if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        test_case = input()
        S, K = test_case.split()
        K = int(K)
        Sint = convert_row_to_int(S)
        PancakeRow.fsize = K
        prow = PancakeRow(Sint, K)

        if prow.all_happy():
            print("Case #{}: {}".format(ti + 1, 0))
            continue
        row_try = [prow]

        max_level = 10000
        level = 0
        STOP = False
        already_tested_pattern = []
        while row_try != [] and level < max_level and not STOP:
            level += 1
            evaluation = [r.eval_state for r in row_try]
            maxi = max(evaluation)
            for counter in range(evaluation.count(maxi)):
                idxmax = evaluation.index(maxi)
                row = row_try.pop(idxmax)
                evaluation.pop(idxmax)
                if row.row in already_tested_pattern:
                    continue
                else:
                    already_tested_pattern.append(row.row)
                for pos in range(0, row.size_row - (K - 1)):
                    new_row = row.flip(pos)
                    if new_row is not None:
                        if new_row.all_happy():
                            print("Case #{}: {}".format(ti + 1, new_row.step))
                            STOP = True
                            break
                        row_try.append(new_row)
                if STOP:
                    break
        if level >= max_level or (row_try == [] and not STOP):
            print("Case #{}: {}".format(ti + 1, IMP))
        # print()
