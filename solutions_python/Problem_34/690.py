import string

inp = open("A-large.in","r")
out = open("A-large.out","w")

content = inp.readlines()

line = content[0]
line = line.split()

L = string.atoi(line[0])
D = string.atoi(line[1])
N = string.atoi(line[2])

inp.close()

Dict =  content[1:D+1]
case = 1

for line in content[D+1:]:
    count = 0
    index = 0
    testStr = []
    test = []
    status = 0
    for x in line:
        if x != "(" and x != ")":
            test.append(x)
            if status == 0:
                testStr.append(test)
                test = []
        else:
            if x == "(":
                status = 1
            else:
                status = 0
                testStr.append(test)
                test = []
    
    for x in Dict:
        index = 0
        for y in x[:-1]:
            if y not in testStr[index]:
                break
            index = index + 1
        else:
            count = count +1
    out.write("Case #" + "%d" % case + ": " + "%d" % count + '\n')
    case = case + 1

inp.close()
out.close()
