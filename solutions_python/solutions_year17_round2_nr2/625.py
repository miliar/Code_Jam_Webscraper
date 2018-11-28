filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round 1B\\B\\B-small-attempt3"

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())


def solve(b, r, y):
    orders = []
    tot = b + r + y
    
    if b < 0 or r < 0 or y < 0:
        return "IMPOSSIBLE"    
    if tot == 0:
        return ''
    if tot == 1:
        return "B"*b+"R"*r+"Y"*y    
    if b > r + y or r > b + y or y > b + r:
        return "IMPOSSIBLE"
    #print b, r, y

    print r, b, y
    
    for rby in range(min([r,b,y])+1):
        rb, by, ry = (r+b-y-rby)/2, (-r+b+y-rby)/2, (r-b+y-rby)/2
        print rby, rb, ry, by, tot
        if (2*(rb+by+ry) == r+b+y-3*rby and min([rb, ry, by, rby]) >= 0):
            if (by != 0):
                orders.append("BRY"*rby+"BR"*rb+"BY"*by+"RY"*ry)
            else:
                if (rby != 0):
                    orders.append("BRY"*rby+"RY"*ry+"BR"*rb)
                else:
                    orders.append("BR"*rb+"YR"*ry)
            break
    
    if orders == []:
        return "IMPOSSIBLE"
    else:
        return orders[0]
    
       
for T in xrange(trials):
    n, r, o, y, g, b, v = map(int, fin.readline().strip().split(' '))
        
    ans = solve(b-o, r-g, y-v)  
    print ans  
    
    fout.write("Case #{0}: {1}\n".format(T+1, ans))
    print "Case #{0} done".format(T+1)
                    
fin.close()
fout.close()