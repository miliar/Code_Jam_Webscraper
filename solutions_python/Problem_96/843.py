def main():
    in_dat = open('B-large.in', 'r')
    in_lines = in_dat.readlines()[1:]
    i = 1
    for line in in_lines:
        line = line.split()
        maxsurp = int(line[1])
        numsurp = 0
        nump = 0
        p = int(line[2])
        scores = map(int,line[3:])
        for score in scores:    
            if score >= 3*p-2: # [3*p-2, 3*p-1, 3*p, 3*p+1, 3*p+2] or score > 28:
                nump += 1
            elif score in range(3*p-4, 3*p-2) and score not in [0,1,29,30]:
                numsurp += 1
        if numsurp > maxsurp:
            nump += maxsurp
        else:
            nump += numsurp
        print "Case #"+str(i)+": "+str(nump)
        i += 1

if __name__ == "__main__":
    main()
