def solve(instance):
    cost, rate, goal = map(float, instance.strip().split())
    time_so_far = 0
    rate_so_far = 2
    prev = goal / rate_so_far
    while True:
        if time_so_far + cost / (rate_so_far) + goal / (rate_so_far + rate) > prev:
            break
        time_so_far += cost / (rate_so_far)
        rate_so_far += rate
        prev = time_so_far + goal / rate_so_far

    return prev

def read_input():
    lines = list(open('B-larg-attempt0.in'))
    num_examples = int(lines[0])
    instances = lines[1:]
    f = open('output.txt', 'w')
    solns = []
    for case, sol in enumerate(map(solve, instances), 1):
        soln = "Case #%(case)s: %(sol)s" % vars()
        print soln
        solns.append(soln)
    f.write('\n'.join(solns))
read_input()
