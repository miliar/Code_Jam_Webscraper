def solvecase(Naomi,Ken,L):
    ans1=0
    ans2=0
    naomi = [float(x) for x in Naomi]
    ken = [float(x) for x in Ken]
    naomi.sort()
    ken.sort()
    naomi2 = naomi.copy()
    ken2 = ken.copy()
    for inde in range(L):
        i = naomi[inde]
        for j in ken:
            if j>i:
                ken.remove(j)
                break
        else:
            ans1 += 1
            ken.remove(ken[0])
    for i in range(L):
        if naomi2[L-1-i]<ken2[L-1-i]:
            naomi2.remove(naomi2[0])
            ken2.remove(ken2[L-1-i])
        else:
            ans2 += 1
            naomi2.remove(naomi2[L-1-i])
            ken2.remove(ken2[L-1-i])
    return (ans2,ans1)

def solve():
    with open(r'd:\D-large.in','r') as infile,open(r'd:\DLoutput.out','w') as outfile:
        numofcase = int(infile.readline().strip())
        for i in range(numofcase):
            L = int(infile.readline().strip())
            Naomi = infile.readline().strip().split()
            Ken = infile.readline().strip().split()
            ans2,ans1 = solvecase(Naomi,Ken,L)
            outfile.write('Case #%d: %d %d\n' % ((i+1),ans2,ans1))
            print('Case #%d done!' % (i + 1))
solve()