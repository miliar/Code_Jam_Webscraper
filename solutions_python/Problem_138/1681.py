input = open('D-large.in', 'r')
output = open('D-large.out', 'w')

test_count = int(input.readline())

for i in range(0, test_count):
    block_count = int(input.readline())
    naomi_strs = input.readline().rstrip().split(' ')
    ken_strs = input.readline().rstrip().split(' ')
    naomi_blocks = []
    ken_blocks = []
    for s in naomi_strs:
        naomi_blocks.append(float(s))
    for s in ken_strs:
        ken_blocks.append(float(s))
    naomi_blocks.sort(reverse=True)
    ken_blocks.sort(reverse=True)
    #print naomi_blocks
    #print ken_blocks
    naomi_win_count = 0
    for ken_block in ken_blocks:
        #print str(naomi_blocks[naomi_win_count]) + ", " + str(ken_block)
        if(naomi_blocks[naomi_win_count] > ken_block):
            naomi_win_count += 1

    ken_win_count = 0
    for naomi_block in naomi_blocks:
        #print str(ken_blocks[ken_win_count]) + ", " + str(naomi_block)
        if(ken_blocks[ken_win_count] > naomi_block):
            ken_win_count += 1

    print naomi_win_count
    print block_count - ken_win_count

    output.write("Case #" + str(i + 1) + ": " + str(naomi_win_count) + " " + str(block_count - ken_win_count) + "\n")

input.close()
output.close()
