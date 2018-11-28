text = open('C-small-attempt1.in', 'r')
n = int(text.readline())
for i in range(0,n):
    line = text.readline()
    line = line.split(' ')
    digits = range(1,len(line[0]))
    cjto = range (int(line[0]), int(line[1].split('\n')[0]) + 1)
    res = []
    for elem in cjto:
        for j in digits:
            move = int(str(elem)[j:]+str(elem)[:j])
            if move == elem:
                continue
            if move in cjto:
                res.append(int(str(elem)[j:]+str(elem)[:j]))
    print "Case #"+str(i+1)+": "+str(len(res)/2)
