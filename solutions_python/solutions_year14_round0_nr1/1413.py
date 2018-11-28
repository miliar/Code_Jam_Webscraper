#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


class OutOfLimit(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class GoogleCodeJam():
    def __init__(self):
        self.file_out = None
        self.data = None

        self.input_data()

    def input_data(self):
        file_in = open(raw_input('Input Filename: '))
        self.file_out = open('result.out', 'w+')

        self.data = file_in.readlines()
        self.data.reverse()
        file_in.close()

    def pop_data(self, do_split=False):
        if do_split:
            return self.data.pop().replace('\n', '').split(' ')
        else:
            return self.data.pop().replace('\n', '')


class QRAMagicTrick(GoogleCodeJam):
    @staticmethod
    def check_t(data):
        if data < 1 or data > 100:
            raise OutOfLimit('T error')

    @staticmethod
    def check_answer(data):
        if data < 1 or data > 4:
            raise OutOfLimit('Answer error')

    @staticmethod
    def check_arrangement(data):
        counter = []
        for i in data:
            for j in data[i]:
                current = int(j)
                if current < 1 or current > 16:
                    raise OutOfLimit('Arrangement value error')
                elif current in counter:
                    raise OutOfLimit('Arrangement value is duplicate')
                else:
                    counter.append(current)

    def run(self):
        t = int(self.pop_data())
        self.check_t(t)

        for i in xrange(0, t):
            answer_1st = int(self.pop_data())
            self.check_answer(answer_1st)

            arrangement_1st = dict()
            arrangement_1st[1] = self.pop_data(True)
            arrangement_1st[2] = self.pop_data(True)
            arrangement_1st[3] = self.pop_data(True)
            arrangement_1st[4] = self.pop_data(True)
            self.check_arrangement(arrangement_1st)

            answer_2nd = int(self.pop_data())
            self.check_answer(answer_2nd)

            arrangement_2nd = dict()
            arrangement_2nd[1] = self.pop_data(True)
            arrangement_2nd[2] = self.pop_data(True)
            arrangement_2nd[3] = self.pop_data(True)
            arrangement_2nd[4] = self.pop_data(True)
            self.check_arrangement(arrangement_2nd)

            result = []
            for key, val in collections.Counter(arrangement_1st[answer_1st] + arrangement_2nd[answer_2nd]).items():
                if val > 1:
                    result.append(key)

            length = len(result)
            if length < 1:
                message = 'Volunteer cheated!'
            elif length > 1:
                message = 'Bad magician!'
            else:
                message = result[0]
            self.file_out.write('Case #%i: %s\r\n' % (i + 1, message))

        self.file_out.close()

if __name__ == '__main__':
    QRAMagicTrick().run()
