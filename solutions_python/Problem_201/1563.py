# -*- coding: utf-8 -*-
import sys

def occupy_sequence_info(sequence_size):
    if sequence_size %2 == 1:
        seq_size_left = seq_size_right = (sequence_size - 1) / 2
    else:
        seq_size_left = sequence_size / 2 - 1
        seq_size_right = sequence_size / 2
    return seq_size_left, seq_size_right

def solve(question):
    stall_count = int(question.split()[0])
    man_count = int(question.split()[1])

    occupied = 0
    empty_sequences = {stall_count: 1}
    max_max = max_min = None
    while occupied < man_count:
        max_empty = max(empty_sequences)
        seq_count = empty_sequences[max_empty]
        del empty_sequences[max_empty]
        seq_size_left, seq_size_right = occupy_sequence_info(max_empty)
        if seq_size_left not in empty_sequences:
            empty_sequences[seq_size_left] = seq_count
        else:
            empty_sequences[seq_size_left] += seq_count
        if seq_size_right not in empty_sequences:
            empty_sequences[seq_size_right] = seq_count
        else:
            empty_sequences[seq_size_right] += seq_count
        occupied += seq_count
        max_max = seq_size_right
        max_min = seq_size_left
    return "%i %i" % (max_max, max_min)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f_in, \
             open(sys.argv[1] + ".out", "w") as f_out:
        count = int(f_in.readline())
        for i in range(count):
            question = f_in.readline().strip()
            solution = solve(question)
            f_out.write("Case #%i: %s\n" % (i+1, str(solution)))
