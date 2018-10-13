INPUT = """3
115
1051
6233"""
import sys
from itertools import permutations

def next_number(N):
    perms = sorted(list(set([int("".join(n)) for n in permutations(str(N)+"0")])))
    print perms
    return perms[perms.index(int(N))+1]
    
def solve_input(input):
    lines = [l.strip() for l in input.split('\n')]
    num_tests = int(lines[0])
    print num_tests
    result = ""
    for line in range(1,num_tests+1):
        print line
        result = "%sCase #%d: %d\n" % (result,
                                       line,
                                       next_number(lines[line]))
    return result

if __name__ == "__main__":
    of = open("cj1ba.out","w")
    try:
        INPUT = open(sys.argv[1],"r").read()
    except:
        pass
    of.write( solve_input(INPUT) )
    of.close()
