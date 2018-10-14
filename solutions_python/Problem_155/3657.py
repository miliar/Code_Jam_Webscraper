def solve(input):
    smax = int(input[0])
    scur = 0
    stot = 0
    friends = 0
    while(stot<smax):
        people = int(input[2+scur])
        stot = stot + people
        scur = scur+1
        needed = (scur - stot)
        if needed > 0:
            friends = friends + needed
            stot = stot+needed
    return friends

with open('a.in', 'r') as fin:
    C = int(fin.readline())
    fout = open('a.out', 'w+')
    for i in range(1, C+1):
        res = "Case #{}: {}\n".format(i, solve(fin.readline()))
        print res
        fout.write(res)
    fin.close()
    fout.close()
