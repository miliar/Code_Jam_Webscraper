#!/usr/bin/python3

import sys
infile = sys.argv[1]
try:
    outfile = sys.argv[2]
except IndexError:
    outfile = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in range(no_lines):
        retval.append(f.readline().rstrip())
    return retval



def get_break(n):
    if n<10:
        return -1
        
    n_s = str(n)
    old_digit = n_s[0]
    retval_s = n_s[0]
    
    for idx, digit in enumerate(n_s[1:]):
        if digit < old_digit:
            retval_s += "0"*(len(n_s)-1-idx)
            return int(retval_s)
        else:
            old_digit = digit
            retval_s += digit
            
    return -1
    
def flip(row, flip_idx, width):
    retval = ""
    for idx, item in enumerate(row):
        if idx >= flip_idx and idx < (flip_idx + width):
            if item == "-":
                item = "+"
            else:
                item = "-"

        retval += item

    print("flip", row, flip_idx, width, "->", retval)

    return retval

        

def is_solved(row):
    retval = row.count("+") == len(row)
    print("is_solved?", row, retval)
    return retval
    
def solve(row, width):
    print("IN  ", row, width)
    cnt = 0
    if is_solved(row):
        print("RET", cnt)
        return cnt

    print("P1", row)    
    while True:
        idx = row.find("-"*width)
        if idx>-1:
            row = flip(row, idx, width)
            cnt += 1
        else:
            break

    if is_solved(row):
        print("RET", cnt)
        return cnt
        
    print("REC", row)
    sols = []
    for idx, item in enumerate(row[:-width]):
        if item == "-":
            new_row = flip(row, idx, width)
            print("TRY", new_row)
            subsol = solve(new_row, width)
            if subsol is not None:
                sols.append(subsol + 1)

    if not sols:
        return None
            
    cnt += min(sols)    
    print("RET", cnt)
    return cnt

def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    out = open(outfile, "w")
    
    for case_idx in range(no_cases):
        line = f.readline().strip()
        row, width = line.split(" ")
        width = int(width)
        sol = solve(row, width)
        if sol is None:
            sol = "IMPOSSIBLE"
            
        out.write("Case #%d: %s\n" % (case_idx+1, sol))
            
    f.close()
    out.close()


def test():
    print(flip("+-+-+-+", 0, 4))
    print(flip("-------", 3, 4))

if __name__ == "__main__":
    main()
#    test()
        

