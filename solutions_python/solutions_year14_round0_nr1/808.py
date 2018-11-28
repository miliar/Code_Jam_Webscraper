t = int(raw_input())
for i in xrange(t):
    arg1, arg2 = [], [] 
    ans1 = int(raw_input()) - 1
    for _ in xrange(4): arg1.append(map(int, raw_input().split())) 
    ans2 = int(raw_input()) - 1
    for _ in xrange(4): arg2.append(map(int, raw_input().split())) 
    bind = set(arg1[ans1]) & set(arg2[ans2]) 
    bind = list(bind) 
    txt = "Case #{}: ".format(i+1) 
    if len(bind) == 1: txt += str(bind[0])
    elif len(bind) > 1: txt += "Bad magician!"
    else: txt += "Volunteer cheated!"
    print txt 
