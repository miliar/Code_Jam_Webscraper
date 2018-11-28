from itertools import combinations
import sys

cnt = 0 
w = int(sys.stdin.readline().strip())

while cnt < w:
    sq1 = []
    row = 0
    ans1 = int(sys.stdin.readline().strip())    
    while row < 4:
        line = sys.stdin.readline()
        line = line.strip().split(' ')
        line = [int (x) for x in line]
        sq1 += [line]
        row += 1
    sq2 = []
    row = 0
    ans2 = int(sys.stdin.readline().strip())    
    while row < 4:
        line = sys.stdin.readline()
        line = line.strip().split(' ')
        line = [int (x) for x in line]
        sq2 += [line]
        row += 1
    #print sq1, sq2
    set1 = set(sq1[ans1-1])
    set2 = set(sq2[ans2-1])
    intersect = list(set1 & set2)
    #print intersect
    cnt+=1
    if len(intersect) == 0 :
        print "Case #"+str(cnt) +": Volunteer cheated!"
    elif len(intersect) == 1:
        print "Case #"+str(cnt) +": "+ str(intersect[0])
    else:
        print "Case #"+str(cnt) +": Bad magician!"
        

