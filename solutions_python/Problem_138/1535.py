#!/usr/bin/python

def solution(case, deceitful_war, war):
    with open("output.txt", "a") as output_file:
        output_file.write("Case #{0}: {1} {2}\n".format(case, deceitful_war, war))
        
def ken_get_elem(ken_blocks, block_naomi):
    iterator = 0
    number = 0.0
    
    while( number < block_naomi and iterator < len(ken_blocks) ):
        number = ken_blocks[iterator]
        iterator = iterator + 1
        
    if number < block_naomi:
        number = ken_blocks.pop(0)
    else:
        ken_blocks.remove(number)
    return number

def play_war(naomi_blocks, ken_blocks, blocks):
    points_naomi = 0
    for i in range(blocks):
        block_naomi = naomi_blocks.pop(0)
        block_ken = ken_get_elem(ken_blocks, block_naomi)
        if block_naomi > block_ken:
            points_naomi = points_naomi + 1
    return points_naomi

def get_larger_elem(ken):
    max_elem = ken[-1]
    return max_elem - 0.00000001
    
def get_larger_than(ken):
    max_elem = ken[-1]
    return ((1.0 - max_elem) / 2) + max_elem

def compara_mins(naomi_blocks, ken_blocks):
    if naomi_blocks[0] > ken_blocks[0]:
        return 1
    else:
        return 0

def play_deceitful_war(naomi_blocks, ken_blocks, blocks):
    points_naomi = 0
    for i in range(blocks):
        if len(naomi_blocks) > 1:
            if compara_mins(naomi_blocks, ken_blocks) == 1:
                told_naomi = get_larger_than(ken_blocks)
                block_naomi = naomi_blocks.pop(0)
                block_ken = ken_get_elem(ken_blocks, told_naomi)
            else:
                told_naomi = get_larger_elem(ken_blocks)
                block_naomi = naomi_blocks.pop(0)
                block_ken = ken_get_elem(ken_blocks, told_naomi)
        else:
            block_naomi = naomi_blocks.pop(0)
            told_naomi = block_naomi
            block_ken = ken_get_elem(ken_blocks, told_naomi)
        
        if block_naomi > block_ken:
            points_naomi = points_naomi + 1
    return points_naomi

with(open("input.txt", "r")) as input_file:
    test_cases = input_file.readline()
    naomi_blocks = []
    ken_blocks = []
    
    for i in range(1, int(test_cases) + 1):
        blocks = input_file.readline()
        naomi_blocks = input_file.readline()
        naomi_blocks = naomi_blocks[:-1]
        naomi_blocks = naomi_blocks.split(' ')
        
        ken_blocks = input_file.readline()
        ken_blocks = ken_blocks[:-1]
        ken_blocks = ken_blocks.split(' ')
        
        naomi_blocks = sorted(list(map(float, naomi_blocks)))
        ken_blocks = sorted(list(map(float, ken_blocks)))
        
        deceitful_war = play_deceitful_war(naomi_blocks[:], ken_blocks[:], int(blocks))
        war = play_war(naomi_blocks, ken_blocks, int(blocks))
        solution(i, deceitful_war, war)
