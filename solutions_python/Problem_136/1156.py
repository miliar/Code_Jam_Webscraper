import sys

DEBUG = True

def solver(c, f, x):
    cookie_rate = 2.0
    best = x / cookie_rate
    farms_to_buy = 0
    costs = [(best, cookie_rate)]
    while True:
        last_cost, last_rate = costs[-1]
        new_rate = last_rate + f
        next_cost = (last_cost - x / last_rate) + c / last_rate + x / new_rate
        if next_cost < last_cost:
            costs.append((next_cost, new_rate))
        else:
            return last_cost


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
        cost, f, x = ssi(rl(), func=float)
        answer = solver(cost, f, x)
        output.append('Case #%d: %.7f\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
