def war(n,k):
    n = [x for x in n]
    k[:]
    #n.sort(reverse = True)
    wins = 0
    for i in k:
        for count, o in enumerate(n):
            if i < o:
                n.pop(count)
                break
        else:
            break
    return len(n)
fin = open("input.in", "r")
fout = open("output.txt", "w")
file = fin.read().split("\n")
file.pop(0)
problemNum = 1
for count, line in enumerate(file):
    if count % 3 == 1:
        namoi = sorted([float(x) for x in line.split()])
    elif count % 3 == 2:
        ken = sorted([float(x) for x in line.split()])
        fout.write("Case #%d: %d %d\n" %(problemNum, len(namoi) - war(namoi, ken), war(ken, namoi)))
        problemNum += 1
fout.close()
fin.close()
