#maxTidy
#Author John Schroder  johnschroder@gmail.com

def isTidy(num):
    if len(num) < 2:
        return True
    if num[1] < num[0]:
        return False
    return isTidy(num[1:])


def maxTidy(num):
    num = str(num)
    if isTidy(num):
        return int(num)
    result = ""
    for i in range(0,len(num)):
        if num[i+1] >= num[i]:
            result += num[i]
        else:
            result += str(int(num[i]) - 1)
            result += "9" * (len(num) - (i+1));
            break
    return int(maxTidy(result))


def process(inputfilename, outputfilename):
    fin = open(inputfilename, "r")
    fout = open(outputfilename, "w")

    t = int(fin.readline());
    caseNumber = 0
    while t > 0:
        caseNumber += 1
        t -= 1
        line = fin.readline()
        n = str(int(line))
        tidy = maxTidy(n)
        fout.write("Case #%d: %s\n" % (caseNumber, str(tidy)))

process("test.in", "test.out")