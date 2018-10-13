import sys


def choose_ken(blocks, chosen_naomi):
    winning_blocks = filter(lambda x: x > chosen_naomi, blocks)

    if winning_blocks:
        b = min(winning_blocks)
    else:
        b = min(blocks)

    return b, filter(lambda x: x != b, blocks)


class SolveDeceitful:
    def __init__(self):
        self.table = {}

    def solve(self, blocks_naomi, blocks_ken):
        key = (tuple(blocks_naomi), tuple(blocks_ken))
        if key in self.table:
            return self.table[key]

        if len(blocks_naomi) == 1:
            if blocks_naomi > blocks_ken:
                self.table[key] = 1
                return 1
            else:
                self.table[key] = 0
                return 0

        best_result = 0
        for block in blocks_naomi:
            # truth
            ken_block, rest_blocks = choose_ken(blocks_ken, block)
            truth = self.solve(filter(lambda b: b != block, blocks_naomi),
                               rest_blocks) + (ken_block < block)

            # lie
            told = max(blocks_ken) - 1e-6
            ken_block, rest_blocks = choose_ken(blocks_ken, told)
            lie = self.solve(filter(lambda b: b != block, blocks_naomi),
                             rest_blocks) + (ken_block < block)


            best_result = max(best_result, max(truth, lie))

        self.table[key] = best_result
        return best_result

    def __call__(self, blocks_naomi, blocks_ken):
        return self.solve(blocks_naomi, blocks_ken)

class SolveWar:
    def __init__(self):
        self.table = {}

    def solve(self, blocks_naomi, blocks_ken):
        key = (tuple(blocks_naomi), tuple(blocks_ken))
        if key in self.table:
            return self.table[key]

        if len(blocks_naomi) == 1:
            if blocks_naomi > blocks_ken:
                self.table[key] = 1
                return 1
            else:
                self.table[key] = 0
                return 0

        best_result = 0
        for block in blocks_naomi:
            # truth
            ken_block, rest_blocks = choose_ken(blocks_ken, block)
            result = self.solve(filter(lambda b: b != block, blocks_naomi),
                                rest_blocks) + (ken_block < block)

            best_result = max(best_result, result)

        self.table[key] = best_result
        return best_result

    def __call__(self, blocks_naomi, blocks_ken):
        return self.solve(blocks_naomi, blocks_ken)


f = sys.stdin

tests = int(f.readline())

for i in range(1,tests+1):
    f.readline() # drop the number of blocks
    blocks_naomi = map(float, f.readline().split())
    blocks_ken = map(float, f.readline().split())

    blocks_naomi.sort()
    blocks_ken.sort()

    tuple(blocks_naomi)
    tuple(blocks_ken)

    s1 = SolveDeceitful()(blocks_naomi, blocks_ken)
    s2 = SolveWar()(blocks_naomi, blocks_ken)

    print "Case #%d: %d %d" % (i, s1, s2)



