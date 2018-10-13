import sys

NUM_DEVICES = 0
NUM_SNAPS = 1

def do_case(case):
    if (case[NUM_SNAPS] + 1) % (1 << case[NUM_DEVICES]) == 0:
        return "ON"
    else:
        return "OFF"

def get_num_cases(lines):
    return int(lines[0])

if __name__ == "__main__":
    lines = open(sys.argv[1], "r").readlines()
    cases = []
    
    for i in xrange(1, get_num_cases(lines) + 1):
        print("Case #%d: %s" % (i, do_case([int(num) for num in lines[i].split()])))

