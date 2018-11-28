t = int(raw_input())
for ab in xrange(1,t+1):
    x,y = map(int,raw_input().split())
    posx = 0
    posy = 0
    count = 1
    o = ""
    if x < 0 :
        while count <= (abs(x)-abs(posx)) :
            posx -= count
            count += 1
            o += "W"
        while posx != x :
            c = abs(x)-abs(posx)
            while c > 0:
                posx -= 1
                count += 2
                o += "EW"
                c -= 1
    else :
        while count <= (abs(x)-abs(posx)) :
            posx += count
            count += 1
            o += "E"
        while posx != x :
            c = x-posx
            while c > 0:
                posx += 1
                count += 2
                o += "WE"
                c -= 1
    if y < 0 :
        while count <=(abs(y)-abs(posy)):
            posy -= count
            count += 1
            o += "S"
        while posy != y:
            c = abs(y) - abs(posy)
            while c > 0:
                posy -= 1
                count += 2
                o += "NS"
                c -= 1
    else :
        while count <=(abs(y)-abs(posy)):
            posy += count
            count += 1
            o += "N"
        while posy != y:
            c = abs(y) - abs(posy)
            while c > 0:
                posy += 1
                count += 2
                o += "SN"
                c -= 1

    print "Case #%d: %s" %(ab,o)
        
        
        
