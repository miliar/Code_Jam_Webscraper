f = open("B-large.in", "r")
s = open("output.txt","w")
t = int (f.readline())
for i in range(0,t):
    c,F,x = f.readline().rstrip('\n').split(' ')
    c = float(c)
    F = float(F)
    x = float(x)
    t = 0.0
    gps = 2.0
    while(True):
        TG = c/gps
        TM = x/gps
        if(t+TM>(t+TG+(x/(gps+F)))):
            t = t+TG
            gps = gps+F
        else:
            t = t+TM
            break
        
    s.write("Case #%d: %.7f\n" % ((i+1),t))
    t = 0.0
    gps = 2.0
    
f.close()
s.close()
