#!/usr/bin/env python

# mv ~/Downloads/A-small-attempt0.in .
# time ./run-task.py < A-small-attempt0.in > A-small-attempt0.out

def r_tiles(i, j, data):
    if data[i][j] == "#":
        if data[i+1][j] == "#" and data[i][j+1]=="#" and data[i+1][j+1]=="#":
            data[i][j] = "/"
            data[i][j+1] = "\\"
            data[i+1][j]   = "\\"
            data[i+1][j+1] = "/"
            return True
        else:
            return False 

    return True

def start_solve(x, y, data):
    for i in range(x-1):
        for j in range(y-1):
            if data[i][j] == "#":
                if not r_tiles(i, j, data):
                    return "Impossible"

    for i in range(x): 
        if "#" in data[i]:
                    return "Impossible"
 
    # check for "#" at boundary (x,y)
 
    for i in range(x):
        data[i] = "".join(data[i])
    data = "\n".join(data)

    return data

def do_solve(in_str):
    return res

def proc_input():
    num_cases = int(raw_input())

    for i in range(num_cases):
        # need to read all parameters
        x, y = [int(n) for n in raw_input().split()]

        data = []
        for row in range(x):
            data.append([char for char in raw_input()])

        out = start_solve(x, y, data)

        print "Case #%i:\n%s" % (i+1, out)       

if __name__ == "__main__":
    proc_input()
