def read_file(filename):
    fp = open(filename)
    lines = fp.readlines()
    return lines


def find_next(filename):
    lines = read_file(filename)
    t = int(lines[0])
    s = ""
    for x in range(1,t+1):
        num = int(lines[x])
        d = digits(num)
        dlist = nextnum(d)
        result = value(dlist)
        s = s + "Case #" + str(x) + ": " + str(result) + "\n"
    return s

def nextnum(d):  
    if is_max_arr(d):
        return minsort(d+[0])
    for i in range(2,len(d)+1):
        sublist = d[len(d)-i:]
        if not is_max_arr(sublist):
            lead = sublist[0]
            newleadind = -1
            for j in range(1,i):
                if newleadind == -1:
                    if sublist[j] > lead:
                        newleadind = j
                else:
                    if sublist[j] > lead and sublist[j] < sublist[newleadind]:
                        newleadind = j
            newlead = sublist[newleadind]
            sublist[newleadind] = lead
            subsub = sublist[1:]
            subsub.sort()
            return d[:len(d)-i] + [newlead] + subsub

def minsort(d):
    d.sort()
    i = 1
    while d[0] == 0:
        d[0] = d[i]
        d[i] = 0
        i = i + 1
    return d


def value(d):
    if len(d) == 1:
        return d[0]
    else:
        return d[len(d)-1]+10*value(d[:(len(d)-1)])

def is_max_arr(d):
    for i in range(len(d)-1,0,-1):
        if d[i] > d[i-1]:
            return False
    return True

def digits(num):
    if num < 10:
        return [num]
    else:
        rem = num % 10
        q = (num - rem) / 10
        d = digits(q)
        d.extend([rem])
        return d

def run(filename):
    a = open("output.txt","w")
    a.write(find_next(filename))

run("B-large.txt")







