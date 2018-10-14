#case 2 

fr = file('B-small-attempt0.in')
fw = file('out_file', 'w')

N = fr.readline()
N = int(N)

num = 1
while num <= N:
    line = fr.readline()
    line = line.split()
    A = int(line[0])
    B = int(line[1])
    K = int(line[2])

    count = 0
    for i in range(A):
        for j in range(B):
            r = i & j
            if r < K:
                count += 1

    fw.write('Case #%s: %s\n'%(num, count))
    num += 1

fr.close()
fw.close()
    

