inp = open('A-large.in', 'r')
out = open('A-large.out', 'w')

def single():
    return inp.readline().strip()

def mult():
    return inp.readline().strip().split()

def multint():
    x = inp.readline().strip().split()
    for a in range(len(x)):
        x[a] = int(x[a])
    return x

def ovation(s):
    need = 0
    total = 0

    for a in range(len(s)):
        cneed = a - total
        if cneed > 0:
            need += cneed
            total += cneed
        total += s[a]

    return need

cases = int(inp.readline().strip())

for r in range(cases):
    line = single()
    t = ''
    for x in range(len(line)):
        if line[x] != ' ':
            t = t + line[x]
        else:
            line = line[x+1:]
            break
    t = int(t)
    s = []
    
    for a in range(t+1):
        s.append(int(line[a]))

    result = ovation(s)    

    print("Case #" + str(r+1) + ": " + str(result))
    out.write("Case #" + str(r+1) + ": " + str(result) + "\n")    

inp.flush()
out.flush()
inp.close()
out.close()
