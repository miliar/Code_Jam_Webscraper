'''
Created on 09.04.2016

@author: dw
'''
import sys



def read_input(filename):
    lines = open(filename).readlines()[1:]
    return [int(line) for line in lines]
        

def process_case(n):
    if n == 0:
        return 'INSOMNIA'
    rem = set('1234567890')
    s = n
    while len(rem) > 0:
        rem -= set(str(s))
        s += n
    return s - n


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = (infile[:-3] if infile.endswith('.in') else infile) + '.out'
    with open(outfile, 'w') as f_out:
        for i, inp in enumerate(read_input(infile)):
            line = 'Case #%d: %s' % (i+1, process_case(inp)) 
            print(line)
            f_out.write(line + '\n')