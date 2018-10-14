import sys

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
            s = read('s', fin)
            s = [int(i) for i in s]
            res = [s[0]]
            # Look for the first discrepency
            for i in range(1, len(s)):
                if s[i - 1] > s[i]:
                    res.extend([9] * (len(s) - i))
                    res[i - 1] -= 1
                    i -= 1
                    while (i >= 1) and res[i] < res[i - 1]:
                        res[i] = 9
                        res[i - 1] -= 1
                        i -= 1
                    break
                res.append(s[i])
            while len(res) > 1 and res[0] == 0:
                res = res[1:]
            fout.write('Case #{}: {}\n'.format(j + 1, ''.join(map(str, res))))