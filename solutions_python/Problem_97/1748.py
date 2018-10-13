import sys

def calculate():
    num = 0
    g = ""
    test_case = int(sys.stdin.readline())
    if not 1 <= test_case <= 50:
        print "invalid number test case"
        sys.exit()
    i = 1
    while(test_case > 0):
        split_line = sys.stdin.readline().replace('\n','').split(' ')
        a = int(split_line[0])
        b = int(split_line[1])
        if not len(str(a)) == len(str(b)) or not 1 <= a <= b <= 1000:
            print "invalid A,B"
            sys.exit()
        if not a == b:
            n = a
            m = b
            while n < m:
                while n < m:
                    #print "("+str(n)+","+str(m)+")"
                    if recycled(n, m):
                        num += 1
                    m -= 1
                m = b
                n += 1
        else:
            if recycled(a, b):
                num += 1
        g += "Case #" + str(i) + ": " + str(num) + "\n"
        i += 1
        test_case -= 1
        num = 0
    return g

def recycled(n, m):
    r = False
    nn = ""
    move = 1
    sn = str(n)
    l = len(sn)
    while move <= l-1:
        nn = sn[l-move:l] + sn[0:l-move]
        if nn == str(m):
            r = True
        move += 1
    
    return r
        

if __name__ == "__main__":
    g = calculate()
    #print g
    sys.stdout.write(g)
