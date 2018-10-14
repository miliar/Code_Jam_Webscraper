import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    ans_1 = int(sys.stdin.readline().strip())
    rows_1 = []
    for j in range(4):
        rows_1.append(sys.stdin.readline().strip())
    ans_2 = int(sys.stdin.readline().strip())
    rows_2 = []
    for j in range(4):
        rows_2.append(sys.stdin.readline().strip())
    common = [c for c in rows_1[ans_1-1].split() if c in rows_2[ans_2-1].split()]
    
    if len(common) == 1:
        print 'Case #'+str(i+1)+': '+common[0]
    elif  len(common) == 0:
        print 'Case #'+str(i+1)+': Volunteer cheated!'        
    elif len(common) > 1:
        print 'Case #'+str(i+1)+': Bad magician!'
    else:
        print 'Case #'+str(i+1)+': Bad coder!'
