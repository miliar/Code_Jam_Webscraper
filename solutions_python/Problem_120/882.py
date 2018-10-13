#!/usr/bin/python

import sys

def solve_problem(r, t):
    #print "Solving: ", r, t
    num = 0
    circles = 0
    ml = t
    while True:
        #print "ml=", ml, "r=", (r+num), "spent:", t-ml
        ml -= (2*(r+num) + 1)
        if ml >= 0:
            circles += 1
            num += 2
        else:
            break
    return circles

def solve(in_file, out_file):
    cases = int(in_file.readline())
    for case in range(0, cases):
        params = [int(num) for num in in_file.readline()[:-1].split(' ')]
        r = params[0]
        t = params[1]
        sol = solve_problem(r, t)
        out_file.write("Case #%d: %s\n" % (case+1, sol))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print u"Error: Invalid number of arguments. Expected 1 and received %d." % (len(sys.argv) - 1)
        sys.exit(2)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'
    in_file = open(input_file_name, 'r')
    out_file = open(output_file_name, 'w')
    solve(in_file, out_file)
    in_file.close()
    out_file.close()

