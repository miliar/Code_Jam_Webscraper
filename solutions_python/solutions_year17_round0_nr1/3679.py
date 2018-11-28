def flip(x):
    if x == '-':
        return '+'
    if x == '+':
        return '-'

def fix(line, i, K):
    if (K > (len(line) - i)):
        return -1
    
    for i in range(i, i + K):
        line[i] = flip(line[i])

def solve(line, K):
    count = 0
    for i in range(len(line)):
        l = line[i]
        if l == '-':
            count += 1
            ret = fix(line, i, K)
            
            if ret == -1:
                return "IMPOSSIBLE"
    return count


filename = 'A-large'


fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
N = int(fin.next())
#print N
for i in range(N):
    line , K = fin.next().split()
    K = int(K)
    line = list(line)
    #print i, line, "K: ", K
    result = solve(line, K)
    #print line
    fout.write("Case #{}: {}\n".format(i+1, result))
    
fin.close()
fout.close()