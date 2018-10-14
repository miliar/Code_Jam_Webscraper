def solve(applauders):
    result = 0
    numApplaudingSoFar = 0
    for i in range(len(applauders)):
        if i <= numApplaudingSoFar:
            numApplaudingSoFar += applauders[i]
        else:
            result += (i - numApplaudingSoFar)
            numApplaudingSoFar += (applauders[i] + 1)      
    return result 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        two_inputs = r.readline().split()
        applauders = [int(x) for x in two_inputs[1]]
        w.write('Case #{0}: {1}\n'.format(str(case), solve(applauders)))

