
#!/usr/bin/env python3

"""
Oversized Pancake Flipper exercise for Code Jam - 2017

Author: Mattia Locatelli
e-mail: mattia.bolob@gmail.com

Developed with Python 3.5.2
"""

import collections

class Surface:

    """
    Implements a surface
    """

    def __init__(self, pan_s, flipper_s):

        self._pancakes_lst = list(pan_s)
        self._len_surf = len(self._pancakes_lst)
        self._flipper_size = flipper_s
        self._end_limit = self._len_surf - self._flipper_size

        counter = collections.Counter(self._pancakes_lst)

        self._blanks = counter['-']
        self._happy = counter['+']
        self._flips = 0
        self._curr_pos = 0
        self._next_pos = 0


    def get_flips(self):
        """
        Return number of flips
        """
        return self._flips


    def _flip_pancakes(self):
        """
        Flips pancakes from current position
        """

        found_blank = False
        next_pos = self._curr_pos

        for i in range(self._curr_pos, self._curr_pos + self._flipper_size):
            if self._pancakes_lst[i] == '-':
                self._pancakes_lst[i] = '+'
                self._blanks -= 1
                self._happy += 1
            else:
                self._pancakes_lst[i] = '-'
                self._blanks += 1
                self._happy -= 1

                if not found_blank:
                    found_blank = True
                    next_pos = i

        self._flips += 1

        if not found_blank:
            try:
                self._curr_pos += self._flipper_size + \
                    self._pancakes_lst[self._curr_pos + self._flipper_size:].index('-')
            except ValueError:
                self._curr_pos = self._len_surf
        else:
            self._curr_pos = next_pos


    def make_happy(self):

        """
        Count number of flips needed
        """

        if self._blanks == 0:
            self._flips = 0
            return

        if self._happy == 0:
            self._flips = (self._len_surf // self._flipper_size) \
                if (self._len_surf % self._flipper_size) == 0 else -1
            return

        self._curr_pos = self._pancakes_lst.index('-')

        while self._blanks > 0 and self._curr_pos < self._end_limit:

            self._flip_pancakes()

        if self._blanks > 0:
            if  self._blanks == self._flipper_size:
                self._flips += 1
            else:
                self._flips = -1


def main():

    """
    Main program entry
    """

    num_t = int(input())  # read a line with a single integer

    for i in range(1, num_t + 1):
        tmp = input().split(" ")
        pan_s, flipper_s = tmp[0], int(tmp[1])
        tmp = Surface(pan_s, flipper_s)

        tmp.make_happy()

        print("Case #{}: {}".format(i, "IMPOSSIBLE" if tmp.get_flips() == -1 else tmp.get_flips()))

if __name__ == '__main__':
    main()
