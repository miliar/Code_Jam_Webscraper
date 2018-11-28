
T = int(raw_input())

for t in range(0,T):
    f_ans = int(raw_input())-1
    f_data = []
    for f in range(0,4):
        f_data.append([int(x) for x in raw_input().split()])
    s_ans = int(raw_input())-1
    s_data = []
    for s in range(0,4):
        s_data.append([int(x) for x in raw_input().split()])
        
    pairs = 0
    value = None
    for n in range(0,4):
        if f_data[f_ans][n] in s_data[s_ans]:
            pairs = pairs + 1
            value = f_data[f_ans][n]
    if pairs == 0:
        print "Case #%d: Volunteer cheated!" %(t+1)
    elif pairs == 1:
        print "Case #%d: %d" %(t+1, value)
    else:
        print "Case #%d: Bad magician!" %(t+1)
        
