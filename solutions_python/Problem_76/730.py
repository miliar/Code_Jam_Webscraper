from sys import stdin, stdout, stderr
from string import rstrip
from itertools import combinations

def failsum(numbers):
    total = 0
    for number in numbers: total=total^number
    return total
input = []
for line in stdin:
    input.append(rstrip(line,'\n'))
nTestCases = int(input[0])
stderr.write("# %s test cases\n############################\n"%nTestCases)
line = 1
while line < len(input):
    N = input[line][0]
    candies = input[line+1].split(' ')
    stderr.write('# Case '+str((line+1)/2)+'\n# '+str(N)+' candies:\n# ')
    candies = [int(candy) for candy in candies]
    for candy in candies: stderr.write(str(candy)+' ')
    stderr.write('\n')
    picks = []
    best = -1
    for n in range(1,len(candies)): picks.extend([_ for _ in combinations(range(len(candies)), n)])
    stderr.write('# '+str(len(picks))+' to try\n')
    for pick in picks:
        unpick = range(len(candies))
        for candy in pick: unpick.remove(candy)
        pick = [candies[candy] for candy in pick]
        unpick = [candies[candy] for candy in unpick]
        picksum = failsum(pick)
        unpicksum = failsum(unpick)
        if picksum == unpicksum:
            realvalue = sum(pick)
            if realvalue > best:
                best=realvalue
                stderr.write('##### NEW BEST: '+str(best)+' #####\n')
    if best==-1: best = 'NO'
    stdout.write("Case #%s: "%((line+1)/2)+str(best)+'\n')
    stderr.write('############################\n')
    line += 2

