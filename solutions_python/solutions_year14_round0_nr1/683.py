#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Trick(object):
    def __init__(self, first_row, first_arrange, second_row, second_arrange):
        self.first_row = first_row
        self.first_arrange = first_arrange
        self.second_arrange = second_arrange
        self.second_row = second_row

    def guess(self, f_out, i):
        candidates_1 = set(self.first_arrange[self.first_row - 1])
        candidates_2 = set(self.second_arrange[self.second_row - 1])
        possible_result = candidates_1.intersection(candidates_2)
        f_out.write('Case #%d: ' % i)
        if len(possible_result) == 1:
            f_out.write(str(possible_result.pop()))
        elif len(possible_result) > 1:
            f_out.write("Bad magician!")
        else:
            f_out.write("Volunteer cheated!")
        f_out.write('\n')
        return None




def main():
    # f_in = open('sample.in')
    # f_out = open('sample.out', 'wb')
    f_in = open('A-small-attempt0.in')
    f_out = open('small.out', 'wb')
    T = int(f_in.readline().strip())
    for i in range(T):
        first_row = int(f_in.readline().strip())
        first_arrange = []
        for j in range(4):
            line = f_in.readline().strip()
            first_arrange.append([int(e) for e in line.split()])
        second_row = int(f_in.readline().strip())
        second_arrange = []
        for j in range(4):
            line = f_in.readline().strip()
            second_arrange.append([int(e) for e in line.split()])
        t = Trick(first_row, first_arrange, second_row, second_arrange)
        t.guess(f_out, i+1)



    f_in.close()
    f_out.close()


if __name__ == '__main__':
    main()

