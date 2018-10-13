rich = "RICHARD"
gab = "GABRIEL"

def main():
    f = open("input.txt", "r")
    
    lines = f.readlines()
    i = 0

    for e in lines:
        if i == 0:
            i = 0
        else:
            print "Case #" + str(i) + ": " + logic(map(int, e.split()))
        i += 1

def logic(info):
    x = info[0]
    r = info[1]
    c = info[2]

    if x-1 > r:
        return rich
    elif x-1 > c:
        return rich
    elif (r*c) % x == 0:
        return gab
    else:
        return rich
 
main()
