from __future__ import print_function

def check(t, p):  
    
    for i in range(0, 3):
        if t[i].replace('T', p)[0] == t[i].replace('T', p)[1] == t[i].replace('T', p)[2] == t[i].replace('T', p)[3] == p \
        or t[0].replace('T', p)[i] == t[1].replace('T', p)[i] == t[2].replace('T', p)[i] == t[3].replace('T', p)[i] == p:
            return True
             
        if t[0].replace('T', p)[0] == t[1].replace('T', p)[1] == t[2].replace('T', p)[2] == t[3].replace('T', p)[3] == p \
        or t[0].replace('T', p)[3] == t[1].replace('T', p)[2] == t[2].replace('T', p)[1] == t[3].replace('T', p)[0] == p:
            return True
    return False

def check_dot(t):
    for i in range(0, 3):
        if '.' in t[i]:
            return True
    return False

ln = 0
data = []
case = 1
with open('A-small-attempt2.in', 'r') as f:
    for line in f:
        data.append(line)
        
cases = data[0]

i = 1
with open('Q_A_output.txt','w') as f:
    while i < len(data):
        
        t = []
        for s in range(0, 4):
            t.append(data[i + s])
    
        if check(t, 'X'):
            print ("Case #%s: X won" % case, file=f)    
        elif check(t, 'O'):
            print ("Case #%s: O won" % case, file=f)
        else:
            if check_dot(t):
                print ("Case #%s: Game has not completed" % case, file=f)
            else:
                print ("Case #%s: Draw" % case, file=f)
        i += 5
        case += 1