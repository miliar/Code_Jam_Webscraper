__author__ = 'Gauthier'

import copy

class DeceitfulWarCase(object):
    def __init__(self, naomi_blocks, ken_blocks):
        self.naomi_blocks = naomi_blocks
        self.ken_blocks = ken_blocks
        self.naomi_blocks.sort(reverse=True)
        self.ken_blocks.sort(reverse=True)

    def find_better_block(self, target_block, blocks):
        prev = None
        for b in blocks:
            if prev and b < target_block:
                break
            else:
                prev = b
        if prev < target_block:
            return None
        return prev

    def find_optimal_block(self, target_block, blocks):
        better_block = self.find_better_block(target_block, blocks)
        if not better_block or better_block < target_block:
            better_block = blocks[-1]
        blocks.remove(better_block)
        return better_block

    def resolve_war(self, naomi_blocks, ken_blocks):
        naomi_score = 0
        ken_score = 0
        for b in naomi_blocks:
            opt_block = self.find_optimal_block(b, ken_blocks)
            if opt_block > b:
                ken_score += 1
            else:
                naomi_score += 1
        return naomi_score

    def has_better_blocks(self, blocks_a, blocks_b):
        for i in range(len(blocks_a)):
            if blocks_a[i] > blocks_b[i]:
                return True
        return False

    def resolve_deceitful_war(self, naomi_blocks, ken_blocks):
        naomi_told = []
        naomi_score = 0
        ken_score = 0
        while self.has_better_blocks(ken_blocks, naomi_blocks):
            ken_blocks.pop(0)
            naomi_blocks.pop(-1)
            ken_score += 1
        while len(naomi_blocks):
            #print better_block, self.ken_blocks[0]
            ken_blocks.pop(-1)
            naomi_blocks.pop(0)
            naomi_score += 1
        return naomi_score



    def resolve(self):
        return self.resolve_deceitful_war(copy.deepcopy(self.naomi_blocks), copy.deepcopy(self.ken_blocks)),\
              self.resolve_war(copy.deepcopy(self.naomi_blocks), copy.deepcopy(self.ken_blocks))

class DeceitfulWar(object):
    def read_input(self):
        fd = open("input.txt")
        lines = fd.readlines()
        self.nb_test_case = int(lines[0])
        lines = lines[1:]
        self.test_cases = []
        for i in range(self.nb_test_case):
            naomi_blocks = map(float, lines[1].strip().split(' '))
            ken_blocks = map(float, lines[2].strip().split(' '))
            self.test_cases.append(DeceitfulWarCase(naomi_blocks, ken_blocks))
            lines = lines[3:]
        fd.close()

def main():
    dw = DeceitfulWar()
    dw.read_input()
    # for dwc in dw.test_cases:
    #     dwc.resolve()
    #     #break
    output = open('output.txt', "w+")
    for i in range(len(dw.test_cases)):
        dwc = dw.test_cases[i]
        (a, b) = dwc.resolve()
        output.write("Case #%d: %d %d\n" % (i + 1, a, b))
    output.close()

if __name__ == "__main__":
    main()