# -*- coding: utf-8 -*-

from __future__ import print_function

read_and_seek = lambda istream, n: tuple(istream.readline().split() for i in xrange(4))[n-1]
get_line = lambda stream: tuple(read_and_seek(stream, int(stream.readline())))
intersection = lambda a, b: tuple(i for i in a if i in b)
res = lambda commons: commons[0] if len(commons) == 1 else ('Bad magician!' if commons else 'Volunteer cheated!')

do_work = lambda istream, ostream: tuple(print('Case #%d: %s' % (i, res(intersection(get_line(istream), get_line(istream)))), file=ostream) for i in xrange(1, int(istream.readline()) + 1))


if __name__ == '__main__':
    import sys
    do_work(sys.stdin, sys.stdout)


import unittest, StringIO

TEST_DATA = '''2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
9 10 11 12
5 14 15 16
13 6 7 8'''

class AcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.istream = file('test.txt', 'r')

    def tearDown(self):
        self.istream.close()

    def test_it(self):
        ostream = StringIO.StringIO()
        do_work(self.istream, ostream)
        v = ostream.getvalue()

        self.assertEqual('''Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!\n''', v)

as_stream = lambda s: StringIO.StringIO(s)

class TestIt(unittest.TestCase):
    def test_get_line(self):
        s = as_stream(TEST_DATA)
        line = get_line(s)
        self.assertEqual(('5', '6', '7', '8'), line)

    def test_read_and_seek(self):
        stream = as_stream(TEST_DATA)
        num = int(stream.readline())
        arr = read_and_seek(stream, num)
        next_num = int(stream.readline())
        next_arr = read_and_seek(stream, next_num)

        self.assertEqual(2, num)
        self.assertEqual(3, next_num)
        self.assertEqual(('5', '6', '7', '8'), tuple(arr))
        self.assertEqual(('5', '14', '15', '16'), tuple(next_arr))

    def test_intersetion(self):
        a = ('5', '6', '7', '8')
        b = ('5', '14', '15', '16')
        self.assertEqual(('5',), intersection(a, b))

    def test_res(self):
        self.assertEqual('5', res(('5',)))
        self.assertEqual('Bad magician!', res(('5', '6')))
        self.assertEqual('Volunteer cheated!', res(tuple()))
