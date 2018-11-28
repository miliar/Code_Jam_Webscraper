def read_word(w):
    return next(w).strip()


def read_int(i, b=10):
    return int(read_word(i), b)


def read_words(ws, d=' '):
    return read_word(ws).split(d)


def read_ints(i, b=10, d=' '):
    return [int(x, b) for x in read_words(i, d)]


def expand_sequence(sequence):
    if sequence[0] == 9 and len(sequence) == 1:
        return [6, 3]

    if sequence[0] == 9 and len(sequence) >= 2:
        if sequence[1] == 6 or sequence[1] <= 3:
            sequence.append(6)
            sequence.append(3)
            return sorted(sequence[1:], reverse=True)

    sequence.append(sequence[0] / 2 + sequence[0] % 2)
    sequence.append(sequence[0] / 2)
    return sorted(sequence[1:], reverse=True)


def solve(file_in, file_out):
    file_in = open(file_in, 'r')
    file_out = open(file_out, "w")
    T = read_int(file_in)

    for case in range(T):
        D = read_int(file_in)
        sequence = read_ints(file_in)

        answer = max(sequence)
        dining_time = 0
        sequence = sorted(sequence, reverse=True)

        while sequence[0] > 3:
            sequence = expand_sequence(sequence)
            dining_time += 1
            if sequence[0] + dining_time < answer:
                answer = sequence[0] + dining_time

        file_out.write("Case #%d: %d\n" % (case+1, answer))

    file_in.close()
    file_out.close()


if __name__ == '__main__':
    file_in_name = "B-small-attempt0.in"
    file_out_name = "B-small-attempt0.out"

    solve(file_in_name, file_out_name)


