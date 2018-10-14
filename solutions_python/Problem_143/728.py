def delim(line):
    items = []
    item = ''
    for c in line:
        if c != ' ':
            item += c
        else:
            items.append(item)
            item = ''
    items.append(item[:-1])
    return items

def strListToInt(items):

    for i in range(len(items)):
        items[i] = int(items[i])
    return items
    

def bitwise(A,B):
    a = bin(A)[2:]
    b = bin(B)[2:]
    if len(a) > len(b):
        b = '0' * (len(a)-len(b)) + b
    if len(b) > len(a):
        a = '0' * (len(b)-len(a)) + a

    s = ''
    for i in range(len(a)):
        if a[i]=='1' and b[i]=='1':
            s += '1'
        else:
            s += '0'
    return int(s,2)

def solve(A,B,K):
    count = 0
    for m in range(A):
        for n in range(B):
            if bitwise(m,n) < K:
                count += 1
    return str(count)

 


f = open("B-small-attempt0.in",'r')
outf = open('probBsmall.txt','w')

lines = f.readlines()
T = int(lines[0]) #number of cases
caseIndex = 1;
for i in range(T):
    line = lines[caseIndex]
    items = strListToInt(delim(line))
    A = items[0]
    B = items[1]
    K = items[2]
    

    caseIndex += 1
    outf.write("Case #" + str(i+1) + ": " + solve(A,B,K) + "\n")
    

outf.close()
