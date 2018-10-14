def run_flip(data):
    seq, flips = data.split(' ')
    flips = int(flips)
    mask = int(''.join(['1' for i in range(int(flips))]) + ''.join(['0' for i in range(len(seq) - int(flips) + 1)]), 2)
    seq_str = seq.replace('+', '0').replace('-', '1')
    seq_int = int(seq_str, 2)

    counter = 0
    for x in range(1, len(seq) - flips + 2):
        mask >>= 1
        # print("{0:b}".format(mask), "{0:b}".format(seq_int))
        if seq_int ^ mask < seq_int:
            counter += 1
            seq_int ^= mask

    if seq_int == 0:
        return counter
    else:
        return "IMPOSSIBLE"


if __name__ == '__main__':
    count = int(input())
    for x in range(count):
        inp = input()
        print("Case #%s: %s" % (x + 1, run_flip(inp)))
