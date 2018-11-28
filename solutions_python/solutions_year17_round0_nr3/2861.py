import sys


def empty_stalls(stalls, pos):
    ls = pos - max(stall for stall in stalls if stall < pos) - 1
    rs = min(stall for stall in stalls if stall > pos) - pos - 1
    return (ls, rs)

def blocks(stalls):
    return [(stalls[i] + 1, stalls[i + 1] - stalls[i] - 1) for i in xrange(len(stalls) - 1)]

def privacy(block):
    size = block[1]
    return ((size - 1) / 2, size / 2)

def new_person(blocks):
    largest_block_index = 0
    largest_block = blocks[largest_block_index]
    for index, block in enumerate(blocks):
        if block[1] > largest_block[1]:
            largest_block = block
            largest_block_index = index
    del blocks[largest_block_index]
    ls, rs = privacy(largest_block)
    blocks[largest_block_index:largest_block_index] = split_block(largest_block)
    return (blocks, (ls, rs))

def split_block(block):
    ls, rs = privacy(block)
    blocks = [(block[0], ls), (block[0] + ls + 1, rs)]
    return [block for block in blocks if block[1] > 0]


def k_persons(N, K):
    blocks = [(1, N)]
    for person in range(K):
        blocks, privacy = new_person(blocks)
    return (max(privacy), min(privacy))


def tests():
    assert empty_stalls([0, 5], 2) == (1, 2)
    assert blocks([0, 5]) == [(1, 4)]
    assert privacy((0, 3)) == (1, 1)
    assert privacy((0, 4)) == (1, 2)
    assert new_person([(1, 4)]) == ([(1, 1), (3, 2)], (1, 2))
    assert new_person(new_person([(1, 4)])[0]) == ([(1, 1), (4, 1)], (0, 1))
    assert k_persons(4, 2) == (1, 0)
    assert k_persons(5, 2) == (1, 0)
    assert k_persons(6, 2) == (1, 1)
    assert k_persons(1000, 1000) == (0, 0)
    assert k_persons(1000, 1) == (500, 499)

if __name__ == "__main__":
    tests()
    with open(sys.argv[1]) as input:
        lines = input.readlines()
    lines = lines[1:]
    for nr, line in enumerate(lines):
        N, K = [int(i) for i in line.split()]
        y, z = k_persons(N, K)
        print "Case #{}: {} {}".format(nr + 1, y, z)