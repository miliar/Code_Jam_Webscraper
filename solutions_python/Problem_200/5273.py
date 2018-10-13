import os
with open(os.path.expanduser("/Users/khansabaat/Downloads/B-small-attempt3.in.txt")) as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]
f2 = open(os.path.expanduser("/Users/khansabaat/Downloads/opfile.txt"),'w')

abc = ''
for i2 in range(1, int(inp[0])+1):
    maxi = 0

    for i in range(0, int(inp[i2])+1):
        n1 = []
        for j in range(0, len(str(i))):
            n1.append(str(i)[j])
        n2 = sorted(n1)
        abc = ''
        for m in range(0, len(n2)):
            abc += n2[m]

        for k in range(0, i):
            if int(abc) > maxi:
                maxi = int(abc)
    print("Case #" + str(i2) + ": " + str(maxi))
    f2.write("Case #" + str(i2) + ": " + str(maxi) + '\n')
f.close()
f2.close()
