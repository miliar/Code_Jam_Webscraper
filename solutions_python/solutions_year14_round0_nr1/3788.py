#! /usr/bin/env python

file_read = open("A-small-attempt1.in")
file_write = open("small.out", 'w+')
T = int(file_read.readline())
for i in range(T):
    row1 = int(file_read.readline()) - 1
    cards1 = [ [ int(k)  for k in file_read.readline().strip().split(' ') ] for j in range(4)]
    row2 = int(file_read.readline()) - 1
    cards2 = [ [ int(k) for k in file_read.readline().strip().split(' ') ] for j in range(4)]
    row_1 = cards1[row1]
    row_2 = cards2[row2]
    if row_1 == row_2 or len(set(row_1).symmetric_difference(set(row_2))) < 6:
        res = "Bad magician!"
    elif len(set(row_1).symmetric_difference(set(row_2))) > 6:
        res = "Volunteer cheated!"
    else:     
        res = set(row_1).intersection(set(row_2)).pop()
    file_write.write("Case #%d: %s\n" %(i + 1, res))
            
    
    
file_read.close()
file_write.close()