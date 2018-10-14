import sys
import numpy as np

def is_empty_line(line):
    return np.all(line=='?')

def solve_case(cake):
    latest_line = np.array('?')
    for i, line in enumerate(cake):
        if is_empty_line(latest_line):
            if not is_empty_line(line):
                cake[:i] = line
        else:
            if is_empty_line(line):
                line[:] = latest_line
        latest_line = line
    for line in cake:
        latect_char = '?'
        for i,c in enumerate(line):
            if latect_char=='?':
                if c!='?': 
                    line[:i] = c 
            else:
                if c=='?':
                    line[i] = latect_char
            latect_char = line[i]
    return "\n".join(["".join(line) for line in cake])


def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    lines = lines[1:]
    for case_num in range(T):
        R,C = [int(i) for i in lines[0].split(" ")]
        test_case_lines = lines[1:][:R]
        lines = lines[1+R:]
        cake = np.array([list(line) for line in test_case_lines])
        ans = solve_case(cake)
        print "Case #%d:\n%s"%(case_num+1,ans)

if __name__ == "__main__":
    main()