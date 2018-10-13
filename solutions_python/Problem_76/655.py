#!/usr/bin/env python
########################  Solve  ########################

def solve(data):
    if reduce(lambda x,y: x ^ y, data):
        return 'NO'
    data.sort()
    return sum(data[1:])
    
########################  Template  ########################
def problem(fin):
    fin.readline()
    return map(int, fin.readline().strip('\n').split(' '))
       
if __name__ == '__main__':
    from sys import argv
    
    fin = open(argv[1])
    fout = open(argv[1].replace("in", "out"), "w")
        
    numLines = int(fin.readline())
    problem_list = [problem(fin) for i in range(numLines)]
    
    solution_list = map(solve, problem_list)

    for i, s in enumerate(solution_list):
        fout.write("Case #%s: %s\n" % (i + 1, s))
