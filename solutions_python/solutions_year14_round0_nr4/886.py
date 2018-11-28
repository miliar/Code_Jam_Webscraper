testcase_count = int(input())
for testcase_index in range(testcase_count):
    block_count = int(input())
    naomi_blocks = [float(block) for block in input().split()]
    naomi_blocks.sort()
    ken_blocks = [float(block) for block in input().split()]
    ken_blocks.sort()

##    print(naomi_blocks)
##    print(ken_blocks)

    # war
    war_points = 0

    naomi_index = 0
    ken_index = 0
    while True:
        if naomi_blocks[naomi_index] < ken_blocks[ken_index]:
            naomi_index += 1
            ken_index += 1
        else:
            ken_index += 1
            war_points += 1
        if ken_index == len(ken_blocks):
            break

    # deceitful war
##    deceitful_points = 0
##    while naomi_blocks:
##        kens_heaviest = ken_blocks.pop()
##        if naomi_blocks[-1] > kens_heaviest:
##            deceitful_points += 1
##            naomi_blocks.pop()
##        else:
##            naomi_blocks.pop(0)

    deceitful_points = 0
    for n in naomi_blocks:
        if ken_blocks[0] > n:
            ken_blocks.pop()
        else:
            deceitful_points += 1
            ken_blocks.pop(0)

    print("Case #%d: %d %d" % (testcase_index + 1, deceitful_points, war_points))
