with open('./B.in','r') as f:
    cases=int(f.readline())
    lines=f.readlines()

inputs=[]

def check(l):
    for i in range(0, len(l) - 1):
        if int(l[i]) > int(l[i+1]):
            return i
    return len(l)

for i in range(cases):
    l = list(lines[i])
    del l[-1]

    while (True):
        pinpoint = check(l)
        if pinpoint == len(l):
            break;
        l[pinpoint] = str(int(l[pinpoint]) - 1)

        for j in range(pinpoint + 1, len(l)):
            l[j] = '9'


    while (l[0] == '0'):
        del l[0]

    print "Case #" + str(i+1) + ": " + ''.join(l) 

