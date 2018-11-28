def representation(xs):
    c = xs[0]
    count = 0
    result = []
    for x in xs:
        if c == x:
            count += 1
        else:
            result.append((c,count))
            c = x
            count = 1
    result.append((c, count))
    return result

#print representation("aabc")

def check(line):
    N = len(line[0])
    #print line
    for l in line:
        if len(l) != N:
            return False
    for i in range(N):
        for l in line:
            #print l[i][0], line[0][i][0] 
            if l[i][0] != line[0][i][0]:
                return False
    return True

def match(line):
    N = len(line[0])
    num = 0
    for i in range(N):
        count = 0
        for l in line:
            count += l[i][1]
        count /= float(len(line))
        count = int(count)
        #print l[i][0], count
        for l in line:
            num += abs(count - l[i][1])
    return num
        
f = open("A-small-attempt0.in", "r")
numTest = int(f.readline().strip())
for i in range(numTest):
    N = int(f.readline().strip())
    line = []
    for j in range(N):
        line.append(representation(f.readline().strip()))

    if check(line):
        
        print "Case #" + str(i + 1) + ": " + str(match(line))
    else:
        print "Case #" + str(i + 1) + ": Fegla Won"

    
        
        
