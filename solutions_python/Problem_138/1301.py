#http://docs.python.org/2/library/heapq.html

import sys
from heapq import *

def heapsort(iterable):
    'Equivalent to sorted(iterable)'
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

str_path="C:/Users/Ricky/Documents/1_CUNY_Queens_College/Courses/2014/Spring2014/CS780_AdvancedProgrammngTechniques/GoogleCodeJam/Q_Round/D-large.in"

with open(str_path) as f:
    test_cases = int(f.readline())
    for test_case in range(test_cases):
        output = ''
        num_blocks = int(f.readline())
        naomi_blocks, ken_blocks = [], []
        line = f.readline()
        for block in line.split():
            naomi_blocks.append(float(block))
        line = f.readline()
        for block in line.split():
            ken_blocks.append(float(block))
        naomi_blocks = heapsort(naomi_blocks)
        ken_blocks = heapsort(ken_blocks)
##        print naomi_blocks
##        print ken_blocks

        naomi_deceit_win = 0
        ken_current_block_pos = 0
        ken_heaviest_block_pos = num_blocks - 1
        #Deceitful War Calcuation
        for i in range(num_blocks):
            if naomi_blocks[i] < ken_blocks[ken_current_block_pos]:
                #Naomi knows that no matter what, she will lose for this round.
                #So she calls out a number just smaller than the heaviest block in Ken's list.
                #Ken will choose the heaviest block to win the round.
                ken_heaviest_block_pos -= 1
            else: #naomi_blocks[i] > ken_blocks[ken_current_block_pos]
                #Naomi has a block that is heavier than the lightest block that Ken owns.
                #So she calls out a number that is higher than Ken's heaviest block.
                #Ken in response will only get rid of the lightest block that he owns.
                #Why?
                #To preseve the heavier blocks for later rounds.
                ken_current_block_pos += 1
                naomi_deceit_win += 1

        #Optimal War Calculation
        naomi_blocks.reverse()
        ken_blocks.reverse()

        naomi_honest_win = 0
        ken_current_block_pos = 0
        ken_lightest_block_pos = num_blocks - 1
        for i in range(num_blocks):
            if naomi_blocks[i] > ken_blocks[ken_current_block_pos]:
            #Naomi will win no matter what for the round.
            #Ken will get rid of the lightest block that he owns.
                naomi_honest_win += 1
                ken_lightest_block_pos -= 1
            else: #naomi_blocks[i] < ken_blocks[ken_current_block_pos]
                ken_current_block_pos += 1

        output = str(naomi_deceit_win) + ' ' + str(naomi_honest_win)
        #http://stackoverflow.com/questions/255147/how-do-i-keep-python-print-from-adding-spaces
        sys.stdout.write('Case #')
        sys.stdout.write(str(test_case+1))
        sys.stdout.write(': ')
        print output
f.close()
