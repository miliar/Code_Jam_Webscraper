def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

def alg(q):    
    [n,pd,pg] = q
    print([n,pd,pg])

    if (pg == 100) and (pd != 100):
        return False
    if (pg == 0) and (pd != 0):
        return False
    
    gcdD = gcd(pd, 100)
    gcdG = gcd(pg, 100)
    numD = pd/gcdD
    denD = 100/gcdD
    numG = pg/gcdG
    denG = 100/gcdG
    print(str(numD)+"/"+str(denD))
    print(str(numG)+"/"+str(denG))

    if (denD > n):
        return False

    return True

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
#    f = open("/home/lawford/Desktop/"+fname+"-small-attempt0.in")
    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
    piece1 = f.readline()
    while piece1 != '':
        if alg([ int(x) for x in piece1.split(' ')[0:] ]):
            result = ['Possible']
        else:
            result = ['Broken']
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
