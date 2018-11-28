from sys import argv

def readInput(fl):
    inputs = []
    for ln in open(fl).readlines():
        inputs.append(ln.strip())
    return inputs

def solve(n_case, ln):
    n_audience = [int(n) for n in ln.split(' ')[1]]
    n_claps = 0
    n_friends = 0
    for shyness,n in enumerate(n_audience):
        if n_claps < shyness: 
            extra_friends = shyness - n_claps
            n_claps += n + extra_friends
            n_friends += extra_friends
        else:
            n_claps += n
    print 'Case #%d: %d' % (n_case + 1, n_friends)

if __name__ == '__main__':
    inputs = readInput(argv[1])
    for n_case, ln in enumerate(inputs[1:]):
        solve(n_case, ln)
