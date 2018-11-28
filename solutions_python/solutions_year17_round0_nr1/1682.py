fin = open("A.in")
fout = open("A.out","w")

t = int(fin.readline())

for trial in range(1,t+1):
    l,x = fin.readline().split()
    x = int(x)
    l = list(l)
    count = 0
    while len(l) >= x:
        if l[0] == '-':
            count += 1
            for i in range(1,x):
                l[i] = '+' if l[i] == '-' else '-'
        l = l[1:]
    if any(i == '-' for i in l):
        res = 'IMPOSSIBLE'
    else:
        res = str(count)
    print(l)
    print("Case #"+str(trial)+": "+res)
    fout.write("Case #"+str(trial)+": "+res+'\n')
