import numpy as np
fi = open("mtin.txt", 'r')
fo = open("mtout.txt",'w+')
inp = fi.read()
inp = inp.split('\n')
T = int(inp[0])
for i in range(T):
    x = 10*i
    a = [int(inp[x+1])-1, int(inp[x+6])-1]
    l1 = np.array([inp[x+2].split(), inp[x+3].split(), inp[x+4].split(), inp[x+5].split()]).astype(int)
    l2 = np.array([inp[x+7].split(), inp[x+8].split(), inp[x+9].split(), inp[x+10].split()]).astype(int)
    res = np.intersect1d(l1[a[0]], l2[a[1]])
    fo.write("Case #%d: " % (i+1))
    if len(res) == 1:
        fo.write("%d\n" % res[0])
    elif len(res) > 1:
        fo.write("Bad magician!\n")
    elif len(res) == 0:
        fo.write("Volunteer cheated!\n")
fi.close()
fo.close()


