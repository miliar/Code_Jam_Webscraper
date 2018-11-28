import itertools

INPUT_FILE = 'inputs/B-small-attempt1.in'
OUTPUT_FILE = 'outputs/B-small-attempt1.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

def expandNumber(n, base):
    retVal = []
    while(n > 0):
        retVal.append(n % base)
        n = int(n / base)
    retVal.reverse()
    return retVal

def glueNumber(l):
    retVal = 0
    for elem in l:
        retVal = retVal * 10 + elem
    return retVal

T = int(f_in.readline().strip())

for i in range(T):
    N = int(f_in.readline().strip())
    expandedNum = expandNumber(N, 10)
    expandedNum.insert(0, 0)
    allPerms = list(itertools.permutations(expandedNum))
    allNumbers = []
    for perm in allPerms:
        allNumbers.append(glueNumber(perm))
    allNumbers.sort(reverse=True)
    nPos = allNumbers.index(N);
    number = 0
    if nPos != 0:
        number = allNumbers[nPos - 1]
    else:
        number = -1
    print("Case #" + str(i + 1) + ": " + str(number) + "\n")
    f_out.write("Case #" + str(i + 1) + ": " + str(number) + "\n")


f_in.close()
f_out.close()