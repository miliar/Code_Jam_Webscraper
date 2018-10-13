def load(f):
    with open(f, 'r') as fh:
        lines = fh.read().split('\n')
    n = int(lines[0])
    arr = []
    for line in lines[1:]:
        if line == '':
            continue
        cake, k = line.split()
        k = int(k)
        cake = parse(cake)
        arr += [[cake, k]]
    assert n == len(arr)
    return arr

def flip(cakes, k, i):
    if i+k > len(cakes) or i < 0:
        raise IndexError('griddle smash')
    cakes[i:i+k] = [1 - c for c in cakes[i:i+k]]
    return cakes

def parse(cake_string):
    return tuple(0 if c == '-' else 1 for c in cake_string)

def flip_lr(cakes, k):
    cakes = list(cakes)
    n = len(cakes)
    flips = []
    for i in range(0, n - k + 1):
        if cakes[i] == 0:
            cakes = flip(cakes, k, i)
            flips += [1]
        else:
            flips += [0]
    if sum(cakes) == len(cakes):
        # success
        return flips
    return None

def run(f):
    output = []
    for i, (cakes, k) in enumerate(load(f)):
        flips = flip_lr(cakes, k)
        if flips is None:
            output += ['Case #%d: Impossible' % (i + 1)]
        else:
            output += ['Case #%d: %d' % (i+1, sum(flips))]
    output = '\n'.join(output)
    
    f2 = f + '.out'
    with open(f2, 'w') as fh:
        fh.write(output)
                 
    print 'wrote output to', f2
    return output