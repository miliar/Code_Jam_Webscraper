
def check(d, o):
   if d['.'] == 0:
        if d['X'] == 4 or (d['X'] == 3 and d['T'] == 1):
            print 'Case #'+o+': X won'
            return True
        elif d['O'] == 4 or (d['O'] == 3 and d['T'] == 1):
            print 'Case #'+o+': O won'
            return True
   return False

def check_win(t, o):
    #check diag
    d = {"X":0, "O":0, "T":0, ".":0}
    t1 = d.copy()
     
    for i in range(4):
        d[t[i][i]]+=1
        
    k = check(d, o)
    if k:
        return True
    d = t1.copy()    
    for i in range(4):
        d[t[i][4-i-1]] += 1
        
    k = check(d, o)
    if k:
        return True
    
    for i in range(4):        
        d = t1.copy()
        for j in range(4):
              d[t[i][j]] += 1
        k = check(d, o)
        if k:
              return True
              
    
    for i in range(4):          
        d = t1.copy()
        for j in range(4):
              d[t[j][i]] += 1
        k = check(d, o)
        if k:
              return True
        
    return False

n = raw_input()
l = [[None]*4 for i in range(4)]
for _t in range(int(n)):
    p = False
    for i in range(4):
        t = raw_input()
        for j in range(4):
            l[i][j] = t[j]
            if t[j] == '.':
                p = True
            
        
    t = raw_input()
    e = str(_t+1)
    won = check_win(l, e )
    if not won and p:
        print "Case #"+e+": Game has not completed"
    elif not won:
        print "Case #"+e+": Draw"
        

