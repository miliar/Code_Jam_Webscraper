def solve(instance):
    row_num1 = int(instance[0].strip())-1
    row_num2 = int(instance[5].strip())-1
    game1 = instance[1:5]
    game2 = instance[6:10]
    row1 = game1[row_num1].strip().split()
    row2 = game2[row_num2].strip().split()
    intersection = set(row1) & set(row2)
    print intersection
    print row_num1, row_num2
    if len(intersection) == 1:
        return list(intersection)[0]
    elif len(intersection) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

def read_input():
    lines = list(open('A-small-attempt0.in'))
    num_examples = int(lines[0])
    lines = lines[1:]
    instances = zip(*[lines[i::10] for i in xrange(10)])
    f = open('output.txt','w')
    solns = []
    for case, sol in enumerate(map(solve, instances),1):
        soln = "Case #%(case)s: %(sol)s" % vars()
        print soln
        solns.append(soln)
    f.write('\n'.join(solns))
read_input()
