# /usr/bin/env python
# -*- coding: utf8 -*-
import math


def is_tidy(n: int) -> bool:
    s = str(n)
    if "0" in s.lstrip("0"):
        return False
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True


# Large input
class Tidy_searcher:
    def __init__(self, size, N):
        self.size = size
        self.N = N
        self.current_tidy = "9" * (self.size + 1)
        self.min_tidy = abs(int(self.current_tidy) - N)

    def search(self, reduct=False):
        minb = "1" * self.size
        if reduct:
            maxb = "1" * (self.size + 1)
        else:
            maxb = "9" * self.size
        diff_min = int(minb) - self.N
        diff_max = int(maxb) - self.N
        if diff_min < 0 and diff_max > 0:
            self._tidy_up(list(minb), self.size - 1, 9)
        else:
            self.size -= 1
            self.search(reduct=True)

    def _tidy_up(self, new, pos, maxi):
        for i in range(1, maxi + 1):
            new[pos] = str(i)
            Ni = int("".join(new))
            diff = abs(Ni - self.N)
            if diff < self.min_tidy and Ni <= self.N and is_tidy(Ni):
                self.min_tidy = diff
                self.current_tidy = Ni
            if pos > 0:
                self._tidy_up(new, pos - 1, i)


if __name__ == '__main__':
    # T = int(input())
    # for ti in range(T):
    #     N = int(input())
    #     for ni in range(N, 0, -1):
    #         if is_tidy(ni):
    #             print("Case #{}: {}".format(ti + 1, ni))
    #             break

    T = int(input())
    for ti in range(T):
        N = int(input())
        if is_tidy(N):
            print("Case #{}: {}".format(ti + 1, N))
        else:
            ns = str(N)
            ts = Tidy_searcher(len(ns), N)
            ts.search()
            print("Case #{}: {}".format(ti + 1, ts.current_tidy))

    # N = 323
    # ns = str(N)
    # ts = Tidy_searcher(len(ns), N)
    # ts.search()
    # print("Case #{}: {}".format(0, ts.current_tidy))
