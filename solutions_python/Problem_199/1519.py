import numpy as np


def side_down(chain):
    new_list = list(chain)
    for i, item in enumerate(new_list):
        if item == '-':
            new_list[i] = '+'
        else:
            new_list[i] = '-'
    chain = ''.join(new_list)
    #print(new_list)
    #print(chain)
    return chain


def flip(pancake, size):
    count = 0
    while "-" in pancake:
        position = pancake.index('-')
        # print(position)
        to_be_flipped = pancake[position:(position + int(size))]
        if position + int(size) > len(pancake):
            return "IMPOSSIBLE"
        else:
            pancake = pancake[0:position] + side_down(to_be_flipped) + pancake[position + int(size):]
            # print("pancake: {}".format(pancake))
            count += 1
    # if "-" not in pancake:
        # print("successfully flipped all pancakes: {}".format(pancake))
    return count


if __name__ == '__main__':
    # print("Case #{}: {}\n".format(1, flip("---+-++-", 3)))
    input_file = open('A-large.in')
    output_file = open('A-large-output.in', 'w')
    lines = [line.rstrip('\n') for line in input_file]
    for i, stack in enumerate(lines):
        if i == 0:
            continue
        else:
            pancake = stack.split()[0]
            size = stack.split()[1]
            output_file.write("Case #{}: {}\n".format(i, flip(pancake, size)))
