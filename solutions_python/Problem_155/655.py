def solvea(prob):
    count = 0
    standing = 0

    problem = prob.split()
    there = problem[1]
    there = list(map(int, list(there)))

    for a in range(0, len(there)):
        if standing < a:
            count += (a-standing)
            standing += (a-standing)
        standing += there[a]

    return count

filename = 'A-large.in'
cases = 0

with open(filename) as f:
    stuff = f.readlines()

cases = int(stuff[0])

for x in range(1, cases+1):
    print("Case #"+str(x)+": "+str(solvea(stuff[x])))