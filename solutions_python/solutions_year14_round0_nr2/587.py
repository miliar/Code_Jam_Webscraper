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

def strListToFloat(items):

    for i in range(len(items)):
        items[i] = float(items[i])
    return items
    

def solve(items):
    c = items[0]
    f = items[1]
    x = items[2]
    r = 2.0
    t = 0
    while True:
        t_buy = c/r + x/(r+f)
        t_not = x/r
        if t_not < t_buy:
            return str(t+t_not)
        else:
            t += c/r
            r += f

 


f = open("B-large.in",'r')
outf = open('cookie_L.txt','w')

lines = f.readlines()
T = int(lines[0]) #number of cases
caseIndex = 1;
for i in range(T):
    line = lines[caseIndex]
    items = strListToFloat(delim(line))
    

    caseIndex += 1
    outf.write("Case #" + str(i+1) + ": " + solve(items) + "\n")
    

outf.close()
