import sys

def main():
    f = open('B-large.in')
    e = enumerate(f)

    count = int(e.next()[1])

    for i in range(count):
        res = test_it(i,e)
        print "Case #%d: %s"%(i+1, res)

def calc(cps, c,x):

    farm = c / cps
    goal = x / cps

    return (farm, goal)

def test_it(idx, e):
    c, f, x = e.next()[1].split()

    c = float(c)
    f = float(f)
    x = float(x)
    cps = 2.0

    farm, goal = calc(cps, c,x)
    best = goal
    base = 0
    #print "%s/%s/%s/%s"%(base,cps,farm,goal)

    while base < best:
        base = base + farm
        cps = cps + f

        farm, goal = calc(cps, c,x)
        #print "%s/%s/%s/%s"%(base,cps,farm,goal)

        


        if base+goal < best:
            best = base+goal


    return best

main()
