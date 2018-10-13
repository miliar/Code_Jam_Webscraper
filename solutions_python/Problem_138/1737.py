from __future__ import print_function

input_file = open('input.txt')
output_file = open('output.txt', 'w')

count = int(input_file.readline())

for i in range(count):
    input_file.readline()
    naomi_blocks_orig = sorted(map(float, input_file.readline().split()))
    ken_blocks_orig = sorted(map(float, input_file.readline().split()))

    # War
    naomi_blocks = naomi_blocks_orig[:]
    ken_blocks = ken_blocks_orig[:]
    naomi_points = 0
    ken_points = 0
    for naomi_block in naomi_blocks:
        try:
            kens_larger = next(x[0] for x in enumerate(ken_blocks) if x[1] > naomi_block)
            kens_reply = ken_blocks.pop(kens_larger)

            if kens_reply > naomi_block:
                ken_points += 1
            else:
                naomi_points += 1
        except StopIteration:
            naomi_points += 1
    naomi_points_war = naomi_points

    # Deceitful war
    naomi_blocks = naomi_blocks_orig[:]
    ken_blocks = sorted(ken_blocks_orig, reverse=True)
    naomi_points = 0
    ken_points = 0

    would_lose = []
    for naomi_block in naomi_blocks:
        try:
            kens_largest_ind = next(x[0] for x in enumerate(ken_blocks) if x[1] < naomi_block)
            ken_blocks.pop(kens_largest_ind)
        except StopIteration:
            would_lose.append(naomi_block)

    ken_blocks = sorted(ken_blocks_orig, reverse=True)
    for naomi_block in naomi_blocks:
        try:
            if naomi_block in would_lose:
                kens_largest_ind = next(x[0] for x in enumerate(ken_blocks) if x[1] > naomi_block)
                kens_largest = ken_blocks.pop(kens_largest_ind)
                ken_points += 1
            else:
                naomi_points += 1
        except StopIteration:
            naomi_points += 1
    naomi_points_deceitful = naomi_points
    print("Case #{0}: {2} {1}".format(i + 1, naomi_points_war, naomi_points_deceitful), file=output_file)
output_file.close()
