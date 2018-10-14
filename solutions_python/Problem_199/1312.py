import re, sys

def min_flips(symb_string, flipper_size):
    pancake_bits = 0
    for index, symb in enumerate(symb_string[::-1]):
        if symb == '-': pancake_bits += 2 ** index
    flipper_bits = 0
    flip_counter = 0
    for i in range(flipper_size):
        flipper_bits += 2 ** i
    while pancake_bits >= flipper_bits:
        while pancake_bits % 2 == 0:
            pancake_bits >>= 1
        pancake_bits ^= flipper_bits
        flip_counter += 1
    if pancake_bits != 0: return 'IMPOSSIBLE'
    return flip_counter

def parse(file_name, outfile_name, func):
    file = open(file_name,"r")
    lines = (line.rstrip('\n') for line in file.readlines())
    file.close()
    cases = int(lines.__next__())
    out = open(outfile_name,"w")
    for i in range(cases):
        args = re.split(' ', lines.__next__())
        args[1] = int(args[1])
        output = func(*args)
        if output == 'IMPOSSIBLE':
            out.write('Case #{}: IMPOSSIBLE\n'.format(i+1))
        else: out.write('Case #{0}: {1}'.format(i+1,output) + '\n')
    out.close()
    return

#usage (run using python3): python A.py 'input_filepath' 'output_filename'

if __name__ == '__main__':
    parse(sys.argv[1], sys.argv[2], min_flips)

    
    
    
