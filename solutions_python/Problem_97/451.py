import sys

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('recout1.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        a, b = f.readline().strip().split()
        inta = int(a)
        intb = int(b)
        values = [str(i) for i in range(int(a), int(b)+1)]
        c = 0
        for i in values:
            arr = []
            for j in range(len(i), 0, -1):
                ans = i[j:]+i[:j]
                ans = int(ans)
                if ans > int(i) and ans >= inta and ans <= intb and ans not in arr:
                    arr.append(ans)
                    c+=1
        output.write(str(c)+"\n")
    output.close()
