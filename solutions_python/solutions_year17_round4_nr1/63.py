

fout = open('out.txt','w')
with open('in.txt') as f:
    T = int(f.readline())
    for case in range(1,T+1):
        line = f.readline()

        line = line.split()
        n = int(line[0])
        p = int(line[1])

        line = f.readline()
        line = line.split()
        line = [int(i) % p for i in line]

        ans = 0
        ans += line.count(0)
        if p == 2:
            ones = line.count(1)
            ans += (ones + 1) / 2
        if p == 3:
            ones = line.count(1)
            twos = line.count(2)
            m = min(ones, twos)
            ans += m
            left = max(ones, twos) - m
            ans += (left + 2) / 3
        if p == 4:
            ones = line.count(1)
            twos = line.count(2)
            threes = line.count(3)
            if twos % 2 == 0:
                ans += twos / 2
                m = min(ones, threes)
                ans += m
                left = max(ones, threes) - m
                ans += (left + 3) / 4
            else:
                ans += twos / 2
                m = min(ones, threes)
                ans += m
                left = max(ones, threes) - m
                ans += (left + 5) / 4
        
        
        str = "Case #%d: %d\n" % (case, ans)
        print str,
        fout.write(str)
fout.close()
