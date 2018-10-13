import argparse

def is_tidy(n):
    N = str(n)
    for i in range(1, len(N)):
        if N[i-1] > N[i]:
            return False
    
    return True

def last_tidy(N):
    for n in xrange(int(N), -1, -1):
        if is_tidy(n):
            return n

    return -1

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
parser.add_argument("output", type=str)
args = parser.parse_args()

with open(args.input, 'r') as input_file, open(args.output, 'w') as output_file:
    input_file.readline()#ignore the number of cases
    for line, N in enumerate(input_file, 1):
        output_file.write("Case #{}: {}\n".format(line, last_tidy(N)))