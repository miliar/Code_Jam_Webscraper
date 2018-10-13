import sys

DEBUG = True

def solver(n, words):
    grouped = [group_chars(word) for word in words]
    base_word = "".join([group[0] for group in grouped[0]])
    for groups in grouped[1:]:
        other_base = "".join([group[0] for group in groups])
        if other_base != base_word:
            return "Fegla Won"
    total_edits = 0
    for i in range(len(grouped[0])):
        counts = [group[i][1] for group in grouped]
        current_min = 1000
        for j in range(min(counts), max(counts) + 1):
            next_min = sum([abs(count - j) for count in counts])
            if next_min < current_min:
                current_min = next_min
        total_edits += current_min
    return total_edits


def group_chars(word):
    current_char = None
    current_count = 0
    groups = []
    for c in word:
        if c != current_char:
            if c is not None:
                groups.append((c, current_count))
            current_char = c
            current_count = 0
        current_count += 1
    groups.append((c, current_count))
    return groups

def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')

    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        n = int(rl())
        words = []
        for i in range(n):
            words.append(rl().strip())
        answer = solver(n, words)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
