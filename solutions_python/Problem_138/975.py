def deceitCompare(n, k):
    naomi = list(n)
    ken = list(k)
    win = 0
    while(len(naomi)>0):
        if naomi[0] > ken[0]:
            win += 1
            naomi.remove(naomi[0])
            ken.remove(ken[0])
        else:
            naomi.remove(naomi[0])
            ken.remove(ken[-1])
    return win
            
def usualCompare(n,k):
    naomi = list(n)
    ken = list(k)
    ken_idx = -1
    win = 0
    
    for i,x in enumerate(naomi):
        ken_dt = [dt for dt in ken[ken_idx + 1:] if dt > x]
        if len(ken_dt) == 0:
            win += len(naomi) - i
            break
        else:
            ken_idx = ken.index(ken_dt[0])
    return win

if __name__ == "__main__":
    infile = 'D:\D-large.in'
    outfile = 'D:\output.txt'
    outlns = []
    
    lns = [ln.strip() for ln in open(infile).readlines() if ln.strip() != '']

    cases = int(lns[0])
    for i in range(cases):
        N = int(lns[i*3 + 1])
        naomi = [float(x) for x in lns[i*3 + 2].split(' ')]
        ken = [float(x) for x in lns[i*3 + 3].split(' ')]
        naomi.sort()
        ken.sort()

        outlns.append('Case #' + str(i+1) + ': ' + str(deceitCompare(naomi, ken)) + ' ' + str(usualCompare(naomi, ken))  + '\n')

    f = open(outfile, 'w')
    f.writelines(outlns)
    f.close()