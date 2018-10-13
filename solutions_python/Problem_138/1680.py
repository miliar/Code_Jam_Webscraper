#!/usr/bin/python
# Input to stdin, output to stdout. 
# Tested on python 2.7.5

import fileinput
input_data = list() 
for line in fileinput.input():
    input_data.append(line)

class SolTestCase: 
    ken_blocks = list()
    naomi_blocks = list()
    def __init__(self, raw_input_lines, starting_index):
        self.naomi_blocks = sorted([float(x) for x in 
                                    raw_input_lines[starting_index + 1].split()])
        self.ken_blocks = sorted([float(x) for x in 
                                  raw_input_lines[starting_index + 2].split()])
    def select_ken_block(self, naomi_tell):
        for i in range(0, len(self.ken_blocks)):
            val = self.ken_blocks[i]
            if (val > naomi_tell):
                del self.ken_blocks[i]
                return val
        val = self.ken_blocks[0]
        del self.ken_blocks[0]
        return val
    def select_naomi_block(self):
        kens_highest = self.ken_blocks[-1]
        naomi_highest = self.naomi_blocks[-1]
        if (kens_highest < naomi_highest):
            kens_lowest = self.ken_blocks[0]
            for i in range(0, len(self.naomi_blocks)):
                naomi_lowest = self.naomi_blocks[i]
                if (naomi_lowest > kens_lowest):
                    del self.naomi_blocks[i]
                    return naomi_lowest, naomi_highest + .00000101
        val = self.naomi_blocks[0]
        del self.naomi_blocks[0]
        return val, kens_highest -.00000101
    def dec_war(self):
        ken_score = 0
        naomi_score = 0
        while (len(self.ken_blocks) > 0): 
            naomi_best, naomi_tell = self.select_naomi_block()
            assert(naomi_tell < 1.0)
            assert(naomi_tell > 0.0)
            ken_best = self.select_ken_block(naomi_tell)
            if (naomi_best > ken_best):
                assert(naomi_tell > ken_best)
                naomi_score += 1
            else:
                assert(not (naomi_tell > ken_best))
                ken_score += 1
        return naomi_score
    def war(self):
        ncopy = [ x for x in self.naomi_blocks ];
        kcopy = [ x for x in self.ken_blocks ];
        ken_score = 0
        naomi_score = 0
        while (len(self.ken_blocks) > 0): 
            naomi_best = self.naomi_blocks[-1]
            del self.naomi_blocks[-1]
            ken_best = self.select_ken_block(naomi_best)
            if (naomi_best > ken_best):
                naomi_score += 1
            else:
                ken_score += 1
        self.naomi_blocks = ncopy;
        self.ken_blocks = kcopy;
        return naomi_score
    def output(self, case_num):
        war_out = self.war()
        dec_out = self.dec_war()
        print ("Case #{0}: {1} {2}".format(case_num, dec_out, war_out))
               
test_cases = int(input_data[0])
cur_row = 1
for i in range(0, test_cases):
    case = SolTestCase(input_data, cur_row)
    case.output(i + 1)
    cur_row += 3
    
