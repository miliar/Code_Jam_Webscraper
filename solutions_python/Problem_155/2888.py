in_file = open('A-large.in', 'r')
out_file = open('AoutL.txt', 'w')

n = int(in_file.readline())

for i in range(n):
    c = in_file.readline()
    cas = c.split()
    sh_max = int(cas[0])
    sh = []
    inv = 0
    tot = 0
    for j in range(sh_max+1):
        sh.append(int(cas[1][j]))
    for k in range(len(sh)):
        while(1):
            if k > tot:
                tot = tot + 1
                inv = inv +1
            if k <= tot:
                break
        tot = tot + sh[k]

    out_file.write("Case #" + str(i+1) + ": " + str(inv)+"\n")











out_file.close()
in_file.close()