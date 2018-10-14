def richard(t):
    print ("Case #%d: RICHARD" % t)
    
def gabriel(t):
    print ("Case #%d: GABRIEL" % t)

T = int(raw_input())
for i in range(1,T+1):
    X, R, C = tuple(map(int, raw_input().split(" ")))
    # print (T, X, R, C)
    
    if X == 1:
        gabriel(i)
        continue
    
    if X > 2 and (R == 1 or C == 1):
        richard(i)
        continue
        
    if R*C % X != 0:
        richard(i)
        continue
        
    if X > 2*min(R, C):
        richard(i)
        continue

    if X > 7:
        richard(i)
        continue

    if X == 4 and (R == 2 or C == 2):
        richard(i)
        continue

    gabriel(i)