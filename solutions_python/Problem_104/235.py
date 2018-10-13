import itertools

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

T = int(fin.readline())

for i in range(0, T):
    done = False
    sums = []
    lists = []
    line = fin.readline().split(' ');
    line = [int(x) for x in line]
    line.remove(line[0])
    for j in range(1, len(line)):
        for pt in itertools.combinations(line, j):
            s = sum(pt)
            if s in sums:
                #print pt
                #print lists[sums.index(s)]
                py = lists[sums.index(s)]
                fout.write('Case #' + str(i + 1) + ':\n')
                for x in pt:
                    fout.write(str(x) + ' ')
                fout.write('\n')
                for x in py:
                    fout.write(str(x) + ' ')
                fout.write('\n')
                fout.flush()
                done = True
            else:
                sums.append(s)
                lists.append(pt)
            if done == True:
                break
        if done == True:
            break
fin.close()
fout.close()