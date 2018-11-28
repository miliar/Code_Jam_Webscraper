clo = open("output.txt", 'w')

with open("input.txt") as f:
    t = int(f.readline())
    for test in range(1,t+1):
        n = int(f.readline().strip())
        ans = ""
        st = str(n)
        last = len(st)
        for i in range(len(st)-1,0,-1):
            if st[i]<st[i-1]:
                last = i
                st = st[0:i-1] + str(int(st[i-1])-1) + st[i:]

        for i in range(last,len(st)):
            st = st[0:i] + '9' + st[i+1:]

        clo.write("Case #" + str(test) + ": " + str(int(st)))

        clo.write('\n')