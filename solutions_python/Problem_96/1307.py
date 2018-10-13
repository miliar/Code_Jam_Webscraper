import sys

def solver(n, s, p, scores):
    natural = 0
    surprising = 0
    for score in scores:
        natural_score = 0
        surprising_score = 0
        if score <= 1:
            natural_score = score
            surprising_score = score
        elif score % 3 == 0:
            natural_score = score / 3
            surprising_score = natural_score + 1
        elif score % 3 == 1:
            natural_score = score / 3 + 1
            surprising_score = natural_score
        elif score % 3 == 2:
            natural_score = score / 3 + 1
            surprising_score = natural_score + 1
        if natural_score >= p:
            natural += 1
        elif surprising_score >= p:
            surprising += 1
    better = natural
    for i in xrange(s):
        if surprising > 0:
            better += 1
            surprising -= 1
    return better

def ssi(s):
    """
    space separated integers
    """
    return map(int, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(msg='', off=False):
    if not off:
        sys.stderr.write(str(msg) + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        scores = ssi(rl())
        n = scores.pop(0)
        s = scores.pop(0)
        p = scores.pop(0)
        answer = solver(n, s, p, scores)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
