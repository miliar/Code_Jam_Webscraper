def rideMax(start, k, people, n):
    c = 0
    s = start
    over = False;
    while (c < k and not over):
        if((c + people[s]) <= k):
            c += people[s]
            s = s + 1
            if s == n:
                s = 0
        else:
            over = True
        if (s == start):
           over = True
    return c, s
f = open("C-small-attempt0.in")
case = int(f.readline())
string = ''
for index in range(case):
    line = f.readline().rstrip("\n")
    item = line.split()
    r = int(item[0])
    k = int(item[1])
    n = int(item[2])
    item = f.readline().rstrip("\n").split()
    for i in range(n):
        item[i] = int(item[i])
    money = 0
    start = 0
    for i in range(r):
        r_money, start = rideMax(start, k, item, n)
        money += r_money
    string += "Case #" + str(index+1) + ": " + str(money) + "\n"
    
o = open('C-small-attempt0-o.in', 'w')
o.write(string)
o.close()

