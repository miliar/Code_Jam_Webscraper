t = input()
for i in range(t):
    x,r,c = raw_input().split()
    x = int(x)
    r = int(r)
    c = int(c)
    
    if x >= 7 or x > max(r,c) or (x+1)/2 > min(r,c) or r*c < x or (r*c%x):
        winner = False
    elif x == 1 or x == 2 or x == 3:
        winner = True
    elif x == 4:
        winner = min(r,c) > 2
    elif x == 5:
        winner = not (min (r, c) == 3  and max (r, c) == 5 )
    elif x == 6:
        winner = min(r,c) > 3
    if winner:
        winner = "GABRIEL"
    else:
        winner = "RICHARD"
    print "Case #"+str(i+1)+": "+winner
