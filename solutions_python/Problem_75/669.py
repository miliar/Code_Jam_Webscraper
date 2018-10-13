#!/usr/bin/env python
########################  Solve  ########################

def combine(combinations, lst):
    changed = True
    while (len(lst) > 1) and changed:
        a = lst[-1]
        b = lst[-2]
        changed = False
        for comb in combinations:
            if comb[0] == a:
                if comb[1] == b:
                    lst.pop()
                    lst.pop()
                    lst.append(comb[2])
                    changed = True
                    break;
            if comb[0] == b:
                if comb[1] == a:
                    lst.pop()
                    lst.pop()
                    lst.append(comb[2])
                    changed = True
                    break
                    
    return lst
    
def check(oppos, lst):
    for items in oppos:
        if (items[0] in lst) and (items[1] in lst):
            return []
    return lst
            

def solve(data):
    result = []
    for i in data[2]:
        result.append(i)
        result = combine(data[0], result)
        result = check(data[1], result)
    return "[" + ", ".join(["%c" % i for i in result]) + "]"
    
########################  Template  ########################

def problem(fin):
    items = fin.readline().strip('\n').split(' ')
    items.reverse()
    comb = []
    for i in xrange(int(items.pop())):
        comb.append(items.pop())
    oppos = []
    for i in xrange(int(items.pop())):
        oppos.append(items.pop())
    i = items.pop()
    lst = items.pop()
    return (comb, oppos, lst)
       
if __name__ == '__main__':
    from sys import argv
    
    fin = open(argv[1])
    fout = open(argv[1].replace("in", "out"), "w")
        
    numLines = int(fin.readline())
    problem_list = [problem(fin) for i in range(numLines)]
    
    solution_list = map(solve, problem_list)

    for i, s in enumerate(solution_list):
        fout.write("Case #%s: %s\n" % (i + 1, s))
