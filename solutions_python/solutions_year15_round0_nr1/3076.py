f = open('A-large.in')
#f = open('test_ovation.in')
problems = []
cases = f.readline()

for line in f:
    line = line[:-1]
    problems.append([int(i) for i in line.split()[1]])

def solution(p):
    needed = 0
    for i in xrange(len(p) + 1):
        d = i - sum(p[:i])
        if d >= needed:
            needed = d
    return needed

output = open('ovation.out', 'w+')
for i in xrange(len(problems)):
    p = problems[i]
    output.write('Case #%d: %s\n' %(i+1, solution(p)))
