class CakeRow:
    @staticmethod
    def parse(s):
        h = 0
        j = 0
        for c in reversed(s):
            if c == '+':
                h += 2**j
            j += 1
        h += 2**j
        return CakeRow(h, len(s))

    def __init__(self, h, n):
        self.__h = h
        self.__n = n

    @property
    def h(self):
        return self.__h

    @property
    def n(self):
        return self.__n

    @property
    def is_happy(self):
        return self.h + 1 == 2 ** (self.n+1)

    def __str__(self):
        s = bin(self.h)[3:]
        return s.replace('1', '+').replace('0', '-')

    def flip(self, i, k):
        new_h = self.h ^ int('0'+'0'*i+'1'*k+(self.n-i-k)*'0', 2)
        return CakeRow(new_h, self.n)

    def __hash__(self):
        return self.h

    def __eq__(self, other):
        return self.h == other.h

def solve(s, k):
    #print 'Start for {} {}'.format(s, k)
    cake_row = CakeRow.parse(s)
    n = len(s)
    if cake_row.is_happy:
        return 0
    else:
        new_rows = set()
        processed = set()
        flips = 1
        while True:
            #print flips
            no_changes = True
            rows = {cake_row} if len(new_rows)==0 else new_rows.copy()
            new_rows.clear()
            for cr in rows:
                if cr in processed:
                    continue
                processed.add(cr)
                for i in xrange(n-k+1):
                    new_cr = cr.flip(i, k)
                    #print 'Flip #{} Produce {} from {} by flipping {} from {}'.format(flips, new_cr, cr, k, i)
                    if new_cr.is_happy:
                        return flips
                    new_rows.add(new_cr)
                    no_changes = False
            #print 'Processed ({}):'.format(len(processed))
            #for cr in processed:
            #    print cr
            if no_changes:
                return 'IMPOSSIBLE'
            flips += 1


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        s, k = raw_input().strip().split()
        k = int(k)
        print 'Case #{}: {}'.format(i+1, solve(s, k))


if __name__ == '__main__':
    main()
