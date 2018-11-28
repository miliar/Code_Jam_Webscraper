#!/usr/bin/env python3
import sys
from bisect import bisect_left

def war(num_blocks, naomis_blocks, kens_blocks):
    naomi_score = num_blocks
    
    for x in naomis_blocks:
        idx = bisect_left(kens_blocks, x)
        if idx  != len(kens_blocks):
#            print(x, kens_blocks[idx])
            del kens_blocks[idx]
            naomi_score -= 1
    return naomi_score

def deceiful_war(num_blocks, naomis_blocks, kens_blocks):
    return num_blocks - war(num_blocks, kens_blocks, naomis_blocks)
    

def main(filename):
    with open(filename, 'r') as f:
        testcases = int(f.readline())
        for case_num in range(testcases):
            num_blocks = int(f.readline())
            naomis_blocks = [float(i) for i in f.readline().split()]
            kens_blocks = [float(i) for i in f.readline().split()]

            naomis_blocks.sort()
            kens_blocks.sort()


            # print(naomis_blocks)
            # print(kens_blocks)

            print("Case #{0}: {1} {2}".format(case_num + 1,
                                              deceiful_war(num_blocks,
                                                           naomis_blocks[:],kens_blocks[:]),
                                              war(num_blocks,
                                                  naomis_blocks[:],kens_blocks[:])))
                                              


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
