import re

def parseline(line):
    return re.search('\d+ (.*)', line).group(1)

def casen(case, clap, index):
    for x in case:
        index += 1
        if clap >= index:
            clap += int(x)
        else:
            return False
    return True

def trycase(case):
    index = -1
    clap = 0

    for n in range(0, len(case)):
        if casen(case, n, index):
            return n


i = 0
casecount = input()

for i in range(1, casecount+1):
    print "Case #" + str(i) + ": " + str(trycase(parseline(raw_input().rstrip())))
