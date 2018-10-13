'''
Created on Apr 10, 2015

@author: billyanhuang
'''
fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')
T = int(fin.readline())
for i in range(T):
    fout.write("Case #")
    fout.write(str(i+1))
    fout.write(": ")
    inp = fin.readline().split()
    S = int(inp[0])
    count = 0
    req = 0
    max = 0
    for j in range(S+1):
        req += 1
        count += int(inp[1][j])
        if (req - count) > max:
            max = req - count
    fout.write(str(max))
    fout.write("\n")