'0 for test, 1 for small, 2 for large'
trying = 2

def solve(A, motes):
    if len(motes) == 0:
        return 0
    index = 0
    while index < len(motes) and A > motes[index]:
        A += motes[index]
        index += 1
    choice1 = len(motes) - index
    
    if choice1 <= 0:
        return 0
    
    numAdds = 0
    if A == 1:
        return choice1
    else:
        while A <= motes[index]:
            A += (A-1)
            numAdds += 1
        choice2 = numAdds + solve(A, motes[index:])
    
    if choice1 < choice2:
        return choice1
    else:
        return choice2


if trying == 0:
    fin = open('testA.txt', 'r')
elif trying == 1:
    fin = open('A-small.in', 'r')
else:
    fin = open('A-large.in', 'r')
finput = fin.readlines()
fin.close()
it = iter(finput)
numbCases = (int)(it.next())
output = ""

for case in xrange(numbCases):
    #print str(case+1)
    firstline = it.next().rstrip().split()
    A = int(firstline[0])
    N = int(firstline[1])
    motes = it.next().rstrip().split()
    for i in range(len(motes)):
        motes[i] = int(motes[i])
    motes.sort()
    
    answer = solve(A, motes)
    output += "Case #%d: %d\n" % (case+1, answer)




if trying == 0:
    fout = open('testoutA.txt', 'w')
elif trying == 1:
    fout = open('smallA.txt', 'w')
else:
    fout = open('largeA.txt', 'w')
fout.write(output)
fout.close()