import math
import sys

def print_case(i, s, p, xs):
    count = 0
    for x in xs:
        if math.ceil(float(x) / 3) >= p:
            count += 1
        elif x > 0 and s > 0:
            if x - 3 * p + 4 >= 0:
                count += 1
                s -= 1

    print "Case #%d: %d" % (i, count)
              
def main():
    lines = open(sys.argv[1]).readlines()[1:]
    for i,line in enumerate(lines):
        n , s, p, xs = line.split(' ', 3)
        print_case(i + 1, int(s), int(p), map(int,xs.split()))
    
if __name__ == "__main__":
    main()
