inp = open('in.txt')
out = open('out.txt', 'w')

t = int(inp.readline())
for case in range(t):
    _, data = inp.readline().split()
    
    acc = 0
    needed = 0
    for shyness, people in enumerate(data):
        if acc < shyness:
            needed += shyness - acc
            acc += shyness - acc
        acc += int(people)
        
    out.write('Case #{}: {}\n'.format(case + 1, needed))
out.close()