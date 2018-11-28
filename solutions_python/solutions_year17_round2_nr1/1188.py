import sys

type_mapper = {
    'i': int,
    's': str,
    'f': float,
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
            dist, n_horse = read('i i', fin)
            times = []
            for k in range(n_horse):
                h_start, h_speed = read('f f', fin)
                times.append((dist - h_start) / h_speed)
            speed = dist / max(times)
            
            fout.write('Case #{}: {:.6f}\n'.format(j + 1, speed))