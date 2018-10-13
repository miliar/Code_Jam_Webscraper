import sys
from itertools import permutations

basename = "D-large"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

def war(ken, naomi):
    ntemp = naomi[:]
    ntemp.sort()
    ktemp = ken[:]
    if max(ntemp) < min(ktemp):
        nscore = 0
    elif min(ntemp) > max(ktemp):
        nscore = len(ntemp)
    else:
        nscore = 0
        for nblock in naomi:
            if nblock > max(ktemp):
                nscore += 1
                ktemp.remove(min(ktemp))
            else:
                kblock = min([b for b in ktemp if b > nblock])
                ktemp.remove(kblock)
    return nscore

#def dwar(ken, naomi):
#    ntemp = naomi[:]
#    ntemp.sort()
#    ktemp = ken[:]
#    ktemp.sort()
#    if min(naomi) > max(ken):
#        p = len(naomi)
#    elif max(naomi) < min(ken):
#        p = 0
#    else:
#        p = 0
#        while p <= len(ntemp) - 1 and ntemp[-(p+1):] > ktemp[:(p+1)]:
#            #print("Comparing n:" + str(ntemp[-(p+1):]) + " to k:" + str(ktemp[:(p+1)]))
#            p += 1
#    return p

def dwar(ken, naomi):
    ktemp = ken[:]
    ntemp = naomi[:]
    ktemp.sort()
    ntemp.sort()
    N = len(ktemp)

    if N == 1:
        if ktemp[0] > ntemp[0]:
            return 0
        else:
            return 1
    while N > 0 and len([i for i in range(N) if ktemp[i] < ntemp[i]]) < N:
        ktemp = ktemp[:-1]
        ntemp = ntemp[1:]
        N -= 1
    return N

for case in range(1, test_cases+1):
    N = int(input_file.readline().rstrip())
    Naomi = [float(a) for a in input_file.readline().rstrip().split(" ")]
    Ken = [float(a) for a in input_file.readline().rstrip().split(" ")]

    solution = " ".join([str(dwar(Ken, Naomi)), str(war(Ken, Naomi))])

    # Output all goes below here. Make sure to define var 'solution' 
    output_file.write("Case #" + str(case) + ": " + str(solution))
    if case < test_cases:
        output_file.write('\n')

