input = 'large'

def result(f):
    inp = f.readline().strip().split()
    pancakes = list(inp[0])
    flipper = int(inp[1])

    count = 0
    idx = 0
    while idx + flipper <= len(pancakes):
        if pancakes[idx] == '-':
            count += 1
            for i in range(idx, idx + flipper):
                if pancakes[i] == '-':
                    pancakes[i] = '+'
                else:
                    pancakes[i] = '-'
        idx += 1
    
    for i in range(idx, len(pancakes)):
        if pancakes[i] == '-':
            return 'IMPOSSIBLE'
    
    return count

fin = open(input + '.in', 'r')
fout = open(input + '.out', 'w')
cases = int(fin.readline())
for i in range(cases):
    fout.write("Case #"+str(i+1)+": "+str(result(fin))+"\n")