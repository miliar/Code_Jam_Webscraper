N = int(raw_input())
for _ in range(N):
    arr = raw_input(),raw_input(),raw_input(),raw_input()
    has_dot = '.' in "".join(arr)    
    won = {'X':False,'O':False}

    def check(line):
        if 'O' not in line and '.' not in line: won['X'] = True
        if 'X' not in line and '.' not in line: won['O'] = True        

    for i in range(4):
        check(arr[i])
        check([arr[j][i] for j in range(4)])
    
        d1 = arr[0][0],arr[1][1],arr[2][2],arr[3][3]
        d2 = arr[0][3],arr[1][2],arr[2][1],arr[3][0]
        check(d1)
        check(d2)
            
    if won['X']:
        print "Case #%d: X won" % (_+1)
    elif won['O']:
        print "Case #%d: O won" % (_+1)
    elif has_dot:
        print "Case #%d: Game has not completed" % (_+1)
    else:
        print "Case #%d: Draw" % (_+1)

    raw_input()