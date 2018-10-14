inp = open('B-large.in', 'r')
out = open('B-large.out', 'w')
test = int(inp.readline())

def calc(num, p):
    score, rem = num / 3, num % 3
    surprizable = True
    if rem == 2:
        if score + 2 > 10:
            surprizable = False
        if score + 1 >= p:
            return (True, surprizable, True)
        elif score + 2 >= p:
            return (False, surprizable, True)
        return (False, surprizable, False)
    elif rem == 1:
        if score - 1 < 0 or score + 1 > 10:
            surprizable = False
        if score + 1 >= p:
            return (True, surprizable, True)
        return (False, surprizable, False)
    else:
        if score - 1 < 0 or score + 1 > 10:
            surprizable = False
        if score >= p:
            return (True, surprizable, True)
        elif score + 1 >= p:
            return (False, surprizable, True)
        return (False, surprizable, False) 
        

for i in range(1, test+1):
    data = inp.readline().split(' ')
    data[-1] = data[-1][-1] == '\n' and data[-1][:-1] or data[-1]
    data = [int(num) for num in data]
    N, S, P = data[0], data[1], data[2]
    data = data[3:]
    conf, not_natural_but_surprising, natural, surprisable = [calc(num, P) for num in data], 0, 0, 0
    for elem in conf:
        surprisable += elem[1] and 1 or 0
        natural += elem[0] and 1 or 0
        not_natural_but_surprising += (not elem[0] and elem[1] and elem[2]) and 1 or 0
    res = surprisable >= S and natural + min(S, not_natural_but_surprising) or 0
    out.write("Case #%d: %s\n" %(i, res))
