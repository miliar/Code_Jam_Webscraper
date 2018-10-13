import sys
import numpy

class Game(object):
    def __init__(self, data):
        self.board = numpy.array([list(d) for d in data])

    def status(self):
        if self.test('X'):
            return 'X won'
        elif self.test('O'):
            return 'O won'
        elif '.' not in self.board:
            return 'Draw'
        else:
            return 'Game has not completed'

    def test(self, x):
        w = self.board == 'T'
        tmp = self.board.copy()
        tmp[w] = x
        cmb = [''.join(b) for b in list(tmp.tolist())] + \
              [''.join(b) for b in list(tmp.T.tolist())] + \
              [''.join(tmp.diagonal())] + \
              [''.join(tmp[[3,2,1,0]].diagonal())]
        return x*4 in cmb

data = open(sys.argv[1]).read().splitlines()[1:]
for n,d in enumerate([data[i:i+4] for i in range(0, len(data), 5)]):
    print 'Case #%i: %s' % (n+1, Game(d).status())
