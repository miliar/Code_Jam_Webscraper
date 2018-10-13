def solve(test):
    n, r, o, y, g, b, v = map(int, raw_input().split())

    


    if check(b, o, n, "BO") and check(y, v, n, "YV") and check(r, g, n, "RB"):
        b-=o
        y-=v
        r-=g

        m = max(r, b, y)

        if m > n-m:
            return "IMPOSSIBLE"

        if r > b:
            if b > y:
                p, c1, c2, c3 = "RBY", r, b, y
            elif r > y:
                p, c1, c2, c3 = "RYB", r, y, b
            else:
                p, c1, c2, c3 = "YRB", y, r, b
        else:
            if r > y:
                p, c1, c2, c3 = "BRY", b, r, y
            elif b > y:
                p, c1, c2, c3 = "BYR", b, y, r
            else:
                p, c1, c2, c3 = "YBR", y, b, r

        
        output = p[0:2] * (c1-c3) + p * (c2+c3-c1) + (p[0]+p[2]) * (c1-c2)

        output = output.replace("B", ("BO" * o)+"B", 1)
        output = output.replace("Y", ("YV" * v)+"Y", 1)
        output = output.replace("R", ("RG" * g)+"R", 1)

        print output

    


   

    #print result

def check(col, mix, n, names):
    if mix > col:
        print "IMPOSSIBLE"
        return False
    if n == col + mix:
        if col == mix:
            print names * mix
        else:
            print "IMPOSSIBLE"
        return False
    else:
        if col == mix and mix>0:
            print "IMPOSSIBLE"
            return False
        else:
            return True


def create_array(*sizes):
   return [0 if len(sizes)==1 else create_array(*sizes[1:]) for x in xrange(sizes[0])]



import sys
sys.stdin = open(sys.argv[1] if len(sys.argv) > 1 else "sample.in")

for test in range(input()):
    print "Case #{}:".format(test+1),
    answer = solve(test)
    if answer != None:
        print answer


