import sys
import numpy as np


type_mapper = {
    'i': int,
    's': str,
}

def read(pattern, stream):
    line = stream.readline().strip()
    input = line.split(' ')
    patterns = pattern.split(' ')
    if len(input) != len(patterns):
        raise ValueError('Could not read\n{}\n{}'.format(input, pattern))
    ret = [type_mapper[p](i) for p, i in zip(patterns, input)]
    if len(ret) == 1:
        return ret[0]
    return ret

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError('Usage: script.py <input>')

    input = sys.argv[1]
    output = sys.argv[1].split('.')[0] + '.out'
    with open(input, 'r') as fin, open(output, 'w') as fout:
        t = read('i', fin)
        for j in range(t):
            s, k = read('s i', fin)
            s = [0 if i == '-' else 1 for i in s]
            s = np.asarray(s)

            c = 0
            for i in range(len(s) - k + 1):
                if s[i] == 0:
                    s[i:i+k] = (s[i:i+k] + 1) % 2
                    c += 1
            if np.all(s == 1):
                fout.write('Case #{}: {}\n'.format(j + 1, c))
            else:
                fout.write('Case #{}: {}\n'.format(j + 1, 'IMPOSSIBLE'))