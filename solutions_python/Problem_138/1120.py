import sys

DEBUG = True

def solver(n, ns, ks):
    ns.sort()
    ks.sort()
    return deceitful_war(n, ns, ks), war(n, ns, ks)

def war(n, ns, ks):
    # copy
    ns = ns[:]
    ks = ks[:]
    score = 0
    while ns:
        n_block = ns.pop(0)
        k_block = None
        for block in ks:
            if block > n_block:
                k_block = block
                ks.remove(k_block)
                break
        if k_block is None:
            k_block = ks.pop(0)
            score += 1
    return score

def deceitful_war(n, ns, ks):
    # copy
    ns = ns[:]
    ks = ks[:]
    score = 0
    idx = 0
    while idx < len(ns):
        if ns[idx] < ks[idx]:
            ns.pop(idx)
            ks.pop()
        else:
            idx += 1
    return len(ns)

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
        ns = ssi(rl(), float)
        ks = ssi(rl(), float)
        dw, w = solver(n, ns, ks)
        output.append('Case #%d: %d %d\n' % (c+1, dw, w))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
