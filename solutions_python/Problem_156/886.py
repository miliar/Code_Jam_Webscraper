import math


def solve(seq, steps):
    length = len(seq)
    if length == 0:
        return steps

    seq_eat = []
    max_elem = 0
    max_elem_pos = 0
    for idx in range(length):
        elem = seq[idx]
        if elem > max_elem:
            max_elem = elem
            max_elem_pos = idx
        if elem > 1:
            seq_eat.append(elem - 1)

    if max_elem <= 3:
        return solve(seq_eat, steps + 1)

    seq_spare = seq[:]
    max_elem_half = max_elem * 0.5
    seq_spare[max_elem_pos] = math.ceil(max_elem_half)
    seq_spare.append(math.floor(max_elem_half))

    max_elem_third = math.ceil(max_elem / 3)
    seq_spare3 = seq[:]
    seq_spare3[max_elem_pos] = max_elem_third
    seq_spare3.append(max_elem - max_elem_third)

    return min(
        solve(seq_eat, steps + 1),
        solve(seq_spare, steps + 1),
        solve(seq_spare3, steps + 1)
    )

if __name__ == "__main__":
    f = open('jam_6224486_2.in', 'r')
    fout = open('jam_6224486_2v2.out', 'w')
    example_count = int(f.readline())
    for i in range(example_count):
        nonempty_count = int(f.readline())
        sequence_raw = f.readline().split(" ")
        sequence = []
        for elem in sequence_raw:
            sequence.append(int(elem))

        result_message = "Case #" + str(i + 1) + ": " + str(solve(sequence, 0))
        # print(sequence)
        print(result_message)
        # print()
        fout.write(result_message + '\n')
