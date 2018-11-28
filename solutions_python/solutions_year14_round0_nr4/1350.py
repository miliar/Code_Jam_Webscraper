#!/usr/bin/python
# -*- coding: utf-8 -*-


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


class QRDDeceitfulWar(GoogleCodeJam):
    @staticmethod
    def get_min_diff(li, ref):
        diff = None
        index = None
        for i in xrange(0, len(li)):
            if li[i] <= ref:
                pass
            elif diff is None:
                diff = li[i] - ref
                index = i
            elif li[i] - ref < diff:
                diff = li[i] - ref
                index = i
        return index

    @staticmethod
    def get_min(li):
        mini = None
        index = None
        for i in xrange(0, len(li)):
            if mini is None:
                mini = li[i]
                index = i
            elif mini > li[i]:
                mini = li[i]
                index = i
        return index

    def run(self):
        t = int(self.pop_data())

        for i in xrange(0, t):
            n = int(self.pop_data())
            naomi_blocks = map(float, self.pop_data(do_split=True))
            ken_blocks = map(float, self.pop_data(do_split=True))
            naomi_blocks_, ken_blocks_ = naomi_blocks[:], ken_blocks[:]
            ken_blocks.sort()

            ken_score = 0
            while naomi_blocks:
                naomi = naomi_blocks.pop()

                index = self.get_min_diff(ken_blocks, naomi)
                if index is None:
                    ken_blocks.pop(self.get_min(ken_blocks))
                else:
                    ken_score += 1
                    ken_blocks.pop(index)

            naomi_score = 0
            while ken_blocks_:
                ken = ken_blocks_.pop()

                index = self.get_min_diff(naomi_blocks_, ken)
                if index is None:
                    naomi_blocks_.pop(self.get_min(naomi_blocks_))
                else:
                    naomi_score += 1
                    naomi_blocks_.pop(index)

            self.file_out.write('Case #%i: %i %i\r\n' % (i + 1, naomi_score, n - ken_score))

        self.file_out.close()

if __name__ == '__main__':
    QRDDeceitfulWar().run()
