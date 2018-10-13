f = open('data.txt', 'r')
g = open('data1.txt', 'w')

line = f.readline()
t = int(line)
for i in range(1, t+1):
    line = f.readline()
    linelist = [int(x) for x in line.split()]
    n = linelist[0]
    s = linelist[1]
    p = linelist[2]
    googlers = linelist[3:]
    result = 0
    onlysurp = 0
    onlynotsurp = 0
    for x in googlers:
        if p == 0:
            result += 1
            continue
        elif p == 1:
            if x >= 1:
                result += 1
            continue  
        elif x <= 3*p - 5:
            continue
        elif x >= 3*p - 1:
            result += 1
            continue
        elif 3*p - 3 >= x >= 3*p - 4:
            onlysurp += 1
            continue
        elif x == 3*p - 2:
            result += 1
            onlynotsurp += 1
            continue
    result += min(s, onlysurp)
    if s > n - onlynotsurp:
        result -= (s - (n - onlynotsurp))
    string = "Case #" + str(i) + ": " + str(result) + '\n'
    g.write(string)

f.close()
g.close()
    
