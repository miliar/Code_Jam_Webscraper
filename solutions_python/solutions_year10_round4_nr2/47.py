import sys

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)
    
    def readline(self):
        result = []
        for token in self.fp.readline().split():
            try:
                value = int(token)
            except ValueError:
                value = token
            result.append(value)
        return result

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    cases, = reader.readline()
    for case in range(cases):
        p, = reader.readline()
        missing_numbers = reader.readline()
        prices = []
        for level in xrange(p):
            prices.append(reader.readline())

        # construct the tree
        def best_price(level, offset, missing_numbers):
            level_size = 1 << (level + 1)
            start = offset * level_size
            end = start + level_size
            if level == 0:      # individual game
                if missing_numbers[start] > 0 and missing_numbers[start + 1] > 0:
                    return 0        # we could just not attend
                else:
                    return prices[0][offset]
            else:       # tourney game
                best = None
                if all(missing_numbers[team] > 0 for team in xrange(start, end)):
                    # we can miss this game
                    for team in xrange(start, end):
                        missing_numbers[team] -= 1
                    best = best_price(level - 1, offset * 2, missing_numbers) + \
                           best_price(level - 1, offset * 2 + 1, missing_numbers)
                    for team in xrange(start, end):
                        missing_numbers[team] += 1
                # what if we see this game?
                price = prices[level][offset] + \
                    best_price(level - 1, offset * 2, missing_numbers) + \
                    best_price(level - 1, offset * 2 + 1, missing_numbers)
                if best is None or price < best:
                    best = price
                return best

        opt = best_price(p - 1, 0, missing_numbers)
        print "Case #%d: %d" % (case + 1, opt)
