def process(lst, num):
    n = num
    for i in range(n):
        lst2 = lst[:]
        for j in range(i):
            # cut and put to lst2
            elem = lst2[-1]
            h1 = num - i
            h2 = elem - h1
            for ii in range(len(lst2)):
                if lst2[ii] > h2:
                    lst2.insert(ii, h2);
                    break
            lst2 = lst2[:-1]
        tr = True
        for elem in lst2:
            if elem > num - i:
                tr = False
        if tr:
            return True

    return False

filename = "B-small-attempt5.in"
inpfile = open(filename, 'r')
outfile = open('Boutput_small.txt', 'w')
casenum = int(inpfile.readline().strip())
for case in range(1, casenum + 1):
    line = inpfile.readline().strip()
    line1 = inpfile.readline().strip()
    linelst = line1.split()
    
    D = int(line)
    P = linelst
    lst = []
    for e in linelst:
        lst.append(int(e))
    lst.sort(reverse=False)
    print lst

    ret = 1008

    att = 1
    while 1:
        if process(lst[:], att):
            break
        att += 1
    ret = min(att, ret)

    result = "Case #" + str(case) + ": " + str(att) + "\n"
    print result
    outfile.write(result)
inpfile.close()
outfile.close()


    