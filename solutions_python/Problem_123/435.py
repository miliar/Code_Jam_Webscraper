def check(a, templ, rs):
    if len(templ) == 0:
        return True
    if rs <= 0:
        return False
    temp = templ.pop(0)
    temprs = rs
    if check(a, templ[:], temprs-1):
        return True
    templ.insert(0, temp)

    while rs > 0:
        rs -= 1
        a += a - 1
        if a > templ[0]:
            a += templ.pop(0)
            if len(templ) == 0:
                return True
            while a > templ[0]:
                a += templ.pop(0)
                if len(templ) == 0:
                    return True
            break
    return check(a, templ, rs)
        
def main():
    fin = open("A-large.in", "r")
    fout = open("alarge.out", "w")
    T = int(fin.readline())
    for i in range(T):
        s = fin.readline().split()
        a = int(s[0])
        n = int(s[1])
        s = fin.readline().split()       
        if a == 1:
            fout.write("Case #%d: %d\n" %(i+1, n))
            continue

        l = [int(j) for j in s]
        l.sort()
        
        while (a > l[0]):
            a += l.pop(0)
            if len(l) == 0:
                fout.write("Case #%d: 0\n" % (i+1))
                break
        if len(l) == 0:
            continue
        
        for step in range(1, 70):
            templ = l[:]
            if check(a, templ, step):
                fout.write("Case #%d: %d\n" % (i+1, step))
                break
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
