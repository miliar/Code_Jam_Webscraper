'''
Created on Apr 10, 2015

@author: billyanhuang
'''
fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

T = int(fin.readline())

for i in range(T):
    fout.write("Case #")
    fout.write(str(i+1))
    fout.write(": ")
    
    D = int(fin.readline())
    inp = fin.readline().split()
    ps = [int(inp[j]) for j in range(D)]
    
    min = 1000
    for j in range(1000):
        sum = 0
        for k in range(D):
            sum += (ps[k] - 1)/(j + 1)
        sum += j + 1
        if sum < min:
            min = sum
    
    fout.write(str(min))
    fout.write("\n")
fout.close()