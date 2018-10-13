inp = raw_input()
inp = inp.split('\n')
T = int(inp[0])
case = 0
while T:
    case = case + 1
    cfx = inp[case]
    cfx1 = cfx.split(' ')
    c = float(cfx1[0])
    f = float(cfx1[1])
    x = float(cfx1[2])
    nfarms1 = (x*f/c - 2)/f
    nfarms = int(nfarms1)
    if nfarms < 0:
        nfarms = 0
    answer = 0.0
    for i in range(0,nfarms):
        answer = answer + c/(2+i*f)
    answer = answer + x/(2+nfarms*f)
    print 'Case #'+str(case)+':',answer
    T = T - 1
    
