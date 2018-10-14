Cases = int(raw_input())
for case in range(Cases):
    line = raw_input()
    max_shy, l = line.split(" ")[0], map(int, list(line.split(" ")[1]))
    need = 0
    for i in range(int(max_shy)+1):
        if l[i] != 0:
            if i == 0:
                continue
            else:
                s = sum(l[:i]) + need
                if  s >= i:
                    continue
                else:
                    need += max(0,i - s)
    print "Case #"+str(case+1)+": "+str(need)
