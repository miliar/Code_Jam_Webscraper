input = 'large'

def untidyPos(l):
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return i
    return -1

def mutate(l):
    pos = untidyPos(l)
    while pos != -1:
        l[pos-1] -= 1
        for i in range(pos, len(l)):
            l[i] = 9
        pos = untidyPos(l)

    return l

def result(f):
    v = f.readline().strip()
    l = map(int, list(v))
    return int("".join(map(str, mutate(l))))

fin = open(input + '.in', 'r')
fout = open(input + '.out', 'w')
cases = int(fin.readline())
for i in range(cases):
    fout.write("Case #"+str(i+1)+": "+str(result(fin))+"\n")