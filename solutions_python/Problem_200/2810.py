def minus_one(line):
    if int(line)==1:
        return ""

    if int(line[-1]) == 0:
        return minus_one(line[:-1])+'9'
    else:
        return line[:-1] + str(int(line[-1])-1)


def process(line):
    if line == '':
        return ''
    if len(line) == 1:
        return line
    tidy = True
    num = line[0]
    i = 1
    prenum = line[0]
    search_next=False
    while tidy:
        if len(line)== i:
            return line
        if int(prenum)>int(line[i]):
            tidy = False
        else:
            if int(prenum) == int(line[i]):
                search_next = True
            num = num + line[i]
            prenum = line[i]
            i += 1
    right_part = "9" * (len(line)-len(num))

    if search_next:
        return process(minus_one(num)) +right_part
    else:
        return minus_one(num)+right_part;


with open('b.in') as ins:
    count=int(ins.readline())
    for i in range(1,count+1):
        line = ins.readline()
        print "Case #"+str(i)+": "+process(line.strip())
