T  = int(raw_input())

def fill(pic, x, y):
    if  y == len(pic)-1:
        return False
    elif x == len(pic[0])-1:
        return False
    pic[y][x] = "/"
    if pic[y][x+1] != "#":
        return False
    pic[y][x+1] = "\\"
    if pic[y+1][x] != "#":
        return False
    pic[y+1][x] = "\\"
    if pic[y+1][x+1] != "#":
        return False
    pic[y+1][x+1] = "/"
    return True
    

for case in xrange(1,T+1):
    l,w = map(int,raw_input().split(" "))
    pic = [ [i for i in raw_input()] for _ in xrange(l) ]
    valid = True
    for y in xrange(l):
        for x in xrange(w):
            if pic[y][x] == "#":
                if not fill(pic,x,y):
                    valid = False
                    break
        if not valid:
            break
    print "Case #%d:" %(case,)
    if valid:
        print "\n".join([ "".join(pic[i]) for i in xrange(l)])
    else:
        print "Impossible"
