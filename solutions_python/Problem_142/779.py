import sys


def process_set(strings):
    sequences = []
    xcounts = []
    for string in strings:
        sequence = ''
        counts = []
        index = -1
        crt_char = None
        for char in string:
            if char != crt_char:
                crt_char = char
                sequence+=crt_char
                index += 1
                counts.append(1)
            else:
                counts[index] += 1
        sequences.append(sequence)
        xcounts.append(counts)
        # print counts

    if any((sequence != sequences[0]) for sequence in sequences):
        print "Fegla Won"
        return

    actions = 0
    N = len(strings)
    seq_len = len(sequences[0])
    avg_counts = []
    for i in range(seq_len):
        avg_counts.append(int(round(sum(counts[i] for counts in xcounts)/N)))

    # print "min", avg_counts
    for i in range(seq_len):
        actions += sum(abs(counts[i]-avg_counts[i]) for counts in xcounts)
    print actions


def process_file(filename):
    with open(filename) as f:
        line = f.readline()
        T = int(line)
        for i in range(T):
            N = int(f.readline())
            strings = []
            for j in range(N):
                strings.append(f.readline().rstrip('\n'))
            print "Case #%d:" % (i+1),
            process_set(strings)



if __name__=="__main__":
    if len(sys.argv) != 2:
        print "missing arguments [input_file]"
    process_file(sys.argv[1])
