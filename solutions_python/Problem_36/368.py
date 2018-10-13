import sys, time

sequence = 'welcome to code jam'

sequence_len = len(sequence)

def solve_case(num):
    # Every queue item is a (sequence start index, input start index) pair
    queue = [(0, 0)]
    count = 0
    input = sys.stdin.readline().strip()
    input_len = len(input)
    while len(queue) > 0:
        ssi, isi = queue[0]
        queue = queue[1:]
        if ssi < sequence_len and isi < input_len:
            pos = input.find(sequence[ssi], isi)
            if pos != -1: # Next needed letter found
                queue.extend([
                    (ssi+1, pos+1), # Use found letter
                    (ssi, pos+1) # Don't use found letter
                ])
        elif ssi >= sequence_len and isi >= input_len:
            count = (count+1)%10000
    print "Case #%i: %04i" % (num, count)

def recursive_solve(seq, input):
    seq_len = len(seq)
    input_len = len(input)
    if seq_len == 0 or seq == input:
        return 1
    elif input_len == 0 or seq_len >= input_len:
        return 0
    pivot = input_len / 2
    subinp_a = input[0:pivot]
    subinp_b = input[pivot:]
    count = 0
    for pivot in range(seq_len+1):
        subseq_a = seq[0:pivot]
        subseq_b = seq[pivot:]
        count_a = recursive_solve(subseq_a, subinp_a)
        count_b = recursive_solve(subseq_b, subinp_b)
        count += count_a * count_b
    return count


def solve_case_smart(num):
    input = sys.stdin.readline().strip()
    print "Case #%i: %04i" % (num, recursive_solve(sequence, input)%10000)

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    for n in xrange(N):
        solve_case_smart(n+1)
