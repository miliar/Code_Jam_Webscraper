#/usr/bin/python3



def input_row():
    p = int(input())
    
    arr = []
    for i in range(4):
        arr.append(list(map(int, input().split())))
    
    return arr[p-1]



T = int(input())

for t in range(T):
    
    row1 = input_row()
    row2 = input_row()
    
    poss = set(row1) & set(row2)
    
    if len(poss) == 0:
        print("Case #%d: Volunteer cheated!" % (t+1))
    elif len(poss) == 1:
        print("Case #%d: %d" % (t+1, poss.pop()))
    else:
        print("Case #%d: Bad magician!" % (t+1))
        



