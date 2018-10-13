import sys

def answer(number, answer):
    print("Case #" + str(number) + ": " + str(answer))

def next_smaller(current):
    if (current % 2 == 0):
        return round((current / 2) - 1)
    else:
        return round((current - 1) / 2)
    
def evolve_block(block):
    output = []
    if block[0]%2 == 1:
        if(next_smaller(block[0]) > 0):
            output.append([next_smaller(block[0]), block[1]*2])
    else:
        if(next_smaller(block[0]) + 1 > 0):        
            output.append([next_smaller(block[0])+1, block[1]])
        if(next_smaller(block[0]) > 0):            
            output.append([next_smaller(block[0]), block[1]])
    return output

def block_to_answer(block_length):
    #print(block_length)
    if round(block_length) == 1:
        return 0, 0
    if block_length%2 == 1:
        return (block_length - 1) / 2, (block_length - 1) / 2
    else:
        return block_length / 2, (block_length / 2) - 1

def cat_blocks(blocks, new_blocks):
    
    for i, new_block in enumerate(new_blocks):
        added = 0
        for j, block in enumerate(blocks):
            if(new_block[0] == block[0]):
                blocks[j][1] += new_blocks[i][1]
                added = 1
                break
        if not added:
            blocks.append(new_block)
    return blocks
#store open blocks in the structure [[7,4], [4,6], [3,8], ... [a,b]]
#where a is the length of the block that is open and b is the number
#of blocks of that size
#with the biggest blocks coming first always
def fill_stalls(stalls, people):
    blocks = [ [stalls, 1] ]
#    print("putting", people, 'people into', stalls, 'stalls')
    while blocks[0][1] < people:
        #print(blocks, people)
        people -= blocks[0][1] #the number of stall "blocks" that are being filled
        new_blocks = evolve_block(blocks.pop(0))
        cat_blocks(blocks, new_blocks)
    #print(blocks[0])
    return block_to_answer(blocks[0][0])

case_num = 0
for line in sys.stdin:
    if case_num == 0:
        case_num += 1
        continue
    l = line.strip().split()
    raw_ans = fill_stalls(int(l[0]), int(l[1]))
    answer(case_num, str(round(raw_ans[0])) + ' ' + str(round(raw_ans[1])))
    case_num+= 1
