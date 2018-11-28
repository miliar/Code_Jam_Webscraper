
def isTidy(s):
    for i in range(len(s)-1):
        if(int(s[i])>int(s[i+1])):
            return False
    return True

inputfile = open('B-small-attempt0.in','r')
outputfile = open('small.out','w')
numcases = inputfile.readline()
case = 0
res = ''

for l in inputfile:
    case += 1
    l = l.strip()
    res = l
    if (not isTidy(l)) & (len(l) > 1):
        res = list(l)
        change = 0
        for i in range(len(l)):
            if change == 0:
                if int(l[i]) >= int(l[i + 1]):
                    change = 1
                    res[i] = str(int(l[i])-1)
            else:
                res[i] = '9'
        res = int("".join(res))
    outputfile.write('Case #'+str(case)+": "+str(res)+"\n")