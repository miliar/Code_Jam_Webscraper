
IMPOSSIBLE = 'IMPOSSIBLE'

def parse_pancake_case(s):
    return [1 if a == '+' else 0 for a in s]

def flip(s, start, end):
    s[start : end] = [int(not f) for f in s[start : end]]
    return s

def flip_pancakes(s, k, case):
    s = parse_pancake_case(s)
    flips = 0
    n = len(s)
    for i in range(n - k + 1):
        if s[i] == 0:
            s = flip(s, i, i + k)
            flips += 1
    res = flips if sum(s) == n else IMPOSSIBLE
    return 'Case #{}:\t{}'.format(case + 1, res)

def flip_pancakes_file(path):
    with open(path, 'rb') as f:
        content = f.readlines()[1 : ]
        results = []
        for case, line in enumerate(content):
            s, k = line.split()
            results.append(flip_pancakes(s, int(k), case))
        with open('{}.out'.format(path), 'wb') as f:
            f.write("\n".join(results))

def main():
    path = '/Users/Shaul/Desktop/A-large.in'
    flip_pancakes_file(path)

if __name__ == '__main__':
    main()