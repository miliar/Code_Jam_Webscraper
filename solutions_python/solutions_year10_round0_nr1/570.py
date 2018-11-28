
infile_name = "A-large.in"
outfile_name = "A-large.out"

n = []
t = []

fin = open(infile_name, "r")
nin = int(fin.readline())
for i in range(nin):
    astr = fin.readline()
    a, b = str(astr).split()
    n.append(int(a))
    t.append(int(b))
fin.close()

fout = open(outfile_name, "w")
for i in range(nin):
    now = t[i]  # snap time
    bin = ""
    twoset = ['0', '1']
    while(True):
        bin += str(twoset[now % 2])
        now = now / 2
        if 0 == now:
            break
    res = True
    for j in range(n[i]):
        try:
            if "0" == bin[j]:
                res = False
                break
        except:
            res = False
            break
    if res:
        astr = "Case #%d: ON\n" % (i + 1)
    else:
        astr = "Case #%d: OFF\n" % (i + 1)

    fout.write(astr)
fout.close()
