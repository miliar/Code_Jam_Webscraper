from optparse import OptionParser

def solve_pA(answer_first, answer_second, grid_first, grid_second ):
    possible =  set(grid_first[answer_first-1])
    final = set()
    for n in grid_second[answer_second-1]:
        if n in possible:
            final.add(n)
    if len(final) == 1:
        return str(final.pop())
    elif len(final) == 0:
        return "Volunteer cheated!"
    elif len(final) > 0:
        return "Bad magician!"
        
    
def problem_A(filename):
    with open(filename, 'rb') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        answer_first = int(lines[i*10+1])
        grid_first = [[int(s) for s in lines[i*10 + 2 + r].split(" ")] for r in range(4)]
        answer_second = int(lines[i*10+6])
        grid_second = [[int(s) for s in lines[i*10 + 7 + r].split(" ")] for r in range(4)]        
        print "Case #%d: %s" % (i+1, solve_pA(answer_first, answer_second, grid_first, grid_second ))





if __name__ == "__main__":
    problem_A("A-small-attempt0.in")
