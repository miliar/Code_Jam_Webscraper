
def main():

    f = open("B-large.in")
    w = open("small.out", "w")
    line = f.readline()
    t = int(line.rstrip())
    for x in range(t):
        line = f.readline().rstrip()
        line = line.split(" ")
        line = [int(y) for y in line]
 #       print line
        ngooglers = line[0]
        surptriplets = line[1]
        p = line[2]
        line = line [3:]
        gtp = 0
        countst = 0
        for s in line:
            base = s / 3
            mod = s % 3
            
            if (mod == 2 or mod == 0) and base >0:
                bestscore = base + mod / 2
                if bestscore >= p:
                    gtp += 1
                elif (bestscore +1) >= p:
                    gtp += 1
                    countst += 1
            elif (base + mod/2) >= p and mod == 2:
                gtp += 1
            elif (base + mod) >= p and mod == 2:
                gtp += 1
                countst += 1
            elif (base + mod) >= p:
                gtp += 1
                
        y = surptriplets - countst
        if y < 0:
            gtp = gtp + y            
        output = "Case #%d: %d" % (x+1, gtp)
        print output
        
if __name__ == "__main__":
    main()