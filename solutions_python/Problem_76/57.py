def tobin(val):
    res = [0 for k in range(20)]
    mod = val
    for k in range(1,21):
        res[-k]=mod % 2
        mod = mod/2
    return res

def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        cans = int(f.readline())
        values = map(int,f.readline().split())
        matrix = map(tobin,values)
        if sum([sum([matrix[j][k] for j in range(cans)])%2 for k in range(20)])>0:
            g.write("NO\n")
            continue
        values.sort()
        g.write("%d\n" % (sum(values[1:])))
    f.close()
    g.close()
    
