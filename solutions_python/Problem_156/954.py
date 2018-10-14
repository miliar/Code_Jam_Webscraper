import math

def solve(stacks, mins):
    eattime = stacks[0]
    if eattime <= 3:
        return eattime + mins
    else:
        for i in range(2, int(math.floor(stacks[0] / 2.0)) + 1):
            newstack = [stacks[0] - i] + stacks[1:] + [i]
            newstack.sort(reverse=True)
            if newstack == [6, 6, 6, 6, 5, 5, 4, 4]:
                print mins
            neweattime = newstack[0]
            eattime = min(eattime + mins, neweattime + mins + 1, solve(newstack, mins+1))
    return eattime; 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\B-small-attempt8.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        throwawayline = r.readline() #number of diners, doesn't matter to me
        stacks = [int(x) for x in r.readline().split()] #get array of pancake stacks
        stacks.sort(reverse=True)
        #if case == 4:
        #    solve(stacks, 0)
        w.write('Case #{0}: {1}\n'.format(str(case), solve(stacks, 0)))

