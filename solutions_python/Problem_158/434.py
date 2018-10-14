for tc in range(1, int(raw_input())+1):
    x, r, c = map(int, raw_input().split())
    rwin = False
    
    if x >= 7:
        rwin = True
    
    elif (x+1)/2 > min(r, c): # choose L shape
        rwin = True
        
    elif x > r and x > c: # choose | shape
        rwin = True
        
    elif r*c % x != 0:
        rwin = True
    
    else:
        a = min(r, c)
        if a > 1 and x-a+1 > a: # choose T shape
            rwin = True
    
    if rwin:
        print 'Case #%d: RICHARD' % tc
    else:
        print 'Case #%d: GABRIEL' % tc