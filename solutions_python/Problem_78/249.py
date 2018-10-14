def rl(f):
    return f.readline().strip()

def main():
    inp = open("A-small-attempt3.in")
    out = open("A-small.out", "w")
    
    T = int(rl(inp))
    for c in range(1, T+1):
        n, pd, pg = map(int, rl(inp).split(" "))
        if (pd != 100 and pg == 100) or (pd > 0 and pg == 0):
            print >>out, "Case #%d: Broken" % c
            continue
        if pd == 0:
            print >>out, "Case #%d: Possible" % c
            continue
            
        x = float(100)/float(pd)
        for i in range(1, min(n, pd)+1):
            y = i*x
            if y == int(y) and y <= n:
                print >>out, "Case #%d: Possible" % c
                break
        else:
            print >>out, "Case #%d: Broken" % c
    
    inp.close()
    out.close()

if __name__ == '__main__':
    main()