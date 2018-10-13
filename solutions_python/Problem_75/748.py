from sys import stdin, stdout, stderr
from string import rstrip

def solve(tasks):
    return 0

input = []
for line in stdin:
    input.append(rstrip(line,'\n'))

nTestCases = int(input[0])
stderr.write("# %s test cases\n############################\n"%nTestCases)

line = 1
while line < len(input):
    tokens = input[line].split(' ')
    C = int(tokens.pop(0))
    combos = tokens[0:C]
    combos = [[''.join(list(combo)[0:2]),list(combo)[2]] for combo in combos]
    tokens = tokens[C:len(tokens)]
    D = int(tokens.pop(0))
    opposed = [list(oppose) for oppose in tokens[0:D]]
    tokens = tokens[D:len(tokens)]
    N = int(tokens.pop(0))
    elq = tokens[0]
    stderr.write('# Case '+str(line)+'\n')
    stderr.write('# '+str(C)+' combinations:\n')
    for combo in combos: stderr.write('# '+combo[0]+' > '+combo[1]+'\n')
    stderr.write('# '+str(D)+' oppositions:\n')
    for oppose in opposed: stderr.write('# '+''.join(oppose)+'\n')
    stderr.write('# '+str(N)+' queued elements:\n')
    stderr.write('# '+elq+'\n')
    ell = []
    for el in elq:
        stderr.write('## '+el+' goes on the list\n')
        ell.append(el)
        if len(ell) < 2:  continue
        tail = [ell.pop(len(ell)-2), ell.pop()]
        stderr.write('## End of the list: '+''.join(tail)+'\n')
        replaced = False
        for combo in combos:
            if combo[0] == ''.join(tail):
                stderr.write('## '+''.join(tail)+' combines to form '+combo[1]+'\n')
                ell.append(combo[1])
                replaced = True
                stderr.write('## Element list:\n## '+''.join(ell)+'\n')
                break
            elif combo[0][::-1] == ''.join(tail):
                stderr.write('## '+''.join(tail)+' combines to form '+combo[1]+'\n')
                ell.append(combo[1])
                replaced = True
                stderr.write('## Element list:\n## '+''.join(ell)+'\n')
                break
        if not replaced: ell.extend(tail)
        for oppose in opposed:
            if ell.count(oppose[0]) > 0 and ell.count(oppose[1]) > 0:
                stderr.write('## '+oppose[0]+' and '+oppose[1]+' oppose and clear the list\n')
                ell = []
                continue        
        stderr.write('## Element list:\n## '+''.join(ell)+'\n')
    ells = str(ell).translate(None,"'")
    stdout.write("Case #%s: "%line+ells+'\n')
    stderr.write('############################\n')
    line += 1

