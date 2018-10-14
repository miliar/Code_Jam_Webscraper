def money(r, k, l):
    s = 0
    for i in range(r):
        tmps = 0
        tmpl = []
        while len(l):
            tmps += l[0]
            if tmps > k:
                break
            s += l[0]
            tmpl.append(l[0])
            l.pop(0)
        l += tmpl
        
    return str(s)

fp = open("C-small-attempt1.in")
fpo = open("C-small-1.out", "w")
case = int(fp.readline())

for x in range(case):
    [ri, ki, ni] = fp.readline().split()
    charlist = fp.readline().split()
    fpo.write("Case #" + str(x+1) + ": " + money(int(ri), int(ki), [int(item) for item in charlist]) + "\n")