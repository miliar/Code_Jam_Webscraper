import sys

def next_line():
    return sys.stdin.readline()

def read_case():
    answers = {}
    grids = {}
    for i in range(2):
        answers[i] = int(next_line())
        grids[i] = {}
        for j in range(4):
            grids[i][j] = next_line().split()
    return answers, grids
    

n_cases = int(next_line())
case = 1
for i in range(n_cases):
    answers, grids = read_case()
    l0 = grids[0][answers[0] - 1]
    l1 = grids[1][answers[1] - 1]
    l = set(l0) & set(l1)
    if len(l) == 1:
        reply = list(l)[0]
    elif len(l) > 1:
        reply = "Bad magician!"
    elif len(l) == 0:
        reply = "Volunteer cheated!"

    print "Case #%i: %s" % (case, reply)
    case = case + 1
