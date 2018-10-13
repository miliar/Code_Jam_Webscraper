def listify(c):
    strc = str(c)
    clist = []
    for i in range (len(strc)):
        clist.append(int(strc[i]))
    return clist

with open ('B-small-attempt0.in.txt') as ifile:
    lines = ifile.readlines()

T = int(lines[0])
res = open('out.txt', 'w')
for cases in range(1, T + 1):
    inp = [int(x) for x in lines[cases].split()]
    c = inp[0]

    while 1:
        temp = listify(c)
        clist = listify(c)
        clist.sort()
        if (c < 10) or (temp == clist):
            break
        elif temp != clist:
            c-=1
    printer = 'Case #' + str(cases)+ ': '
    res.write (printer + str(c) + '\n')
res.close()
