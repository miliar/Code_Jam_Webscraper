import os
from queue import Queue

def read_file(filename):
    path = os.path.join('inputs', filename)
    with open(path, 'r') as f:
        return f.readlines()


def write_file(filename, content):
    path = os.path.join('outputs', filename + '.out')
    with open(path, 'w+') as f:
        return f.writelines(content)


def main():
    for in_file in os.listdir('inputs'):
        content = read_file(in_file)
        result = algo(content)
        write_file(in_file, result)


def algo(content):
    size = int(content[0])
    lines = [line.split() for line in content[1:1+size]]
    return format_lines([bfs(seq, int(k)) for seq, k in lines])


def bfs(seq, k):
    queue = Queue()
    seen = set()

    queue.put((seq, 0))
    seen.add(seq)

    while not queue.empty():
        curr_seq, curr_flips = queue.get()
        print (curr_seq, curr_flips)
        if "-" not in curr_seq:
            return curr_flips

        for flip_start in range(len(curr_seq) - k + 1):

            new_seq = flip(curr_seq, flip_start, k)

            if new_seq in seen: continue

            seen.add(new_seq)
            queue.put((new_seq, curr_flips + 1))

    return None


def flip(seq, start, size):
    return seq[:start] + "".join('+' if c == '-' else '-' for c in seq[start:start+size]) + seq[start+size:]


def format_lines(lines):
    return [   "Case #{}: {}\n".format(
            i + 1, "IMPOSSIBLE" if line == None else line
        ) for i, line in enumerate(lines)
    ]

if __name__ == '__main__':
    main()
